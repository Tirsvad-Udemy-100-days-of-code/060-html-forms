"""!
@file capture.py
@brief Runs a screenshot scenario inside the Docker container.

A scenario is a JSON file:
    {
      "services": ["command started in the background", ...],
      "server": "command that starts the web app",
      "base_url": "http://127.0.0.1:5000",
      "viewport": [1100, 800],
      "steps": [
        {"goto": "/"},
        {"fill": ["input[name=name]", "Angela"]},
        {"click": "input[type=submit]"},
        {"screenshot": "name.png", "full_page": false}
      ]
    }

Usage (inside the container): python capture.py scenario.json output_dir
"""

import json
import shlex
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from playwright.sync_api import sync_playwright

STARTUP_TIMEOUT_SECONDS = 30
POLL_INTERVAL_SECONDS = 0.5
LOCAL_URL_PREFIXES = ("http://127.0.0.1:", "http://localhost:")


def wait_for(url: str) -> None:
    """!
    @brief Block until the web app answers.
    @param url Address to poll.
    """
    if not url.startswith(LOCAL_URL_PREFIXES):
        raise ValueError(f"only local addresses are allowed: {url}")
    pause = threading.Event()
    deadline = time.monotonic() + STARTUP_TIMEOUT_SECONDS
    while time.monotonic() < deadline:
        try:
            # The address is checked above to be local, and http is the only scheme.
            urllib.request.urlopen(url, timeout=2)  # nosemgrep
            return
        except urllib.error.HTTPError:
            return
        except OSError:
            pause.wait(POLL_INTERVAL_SECONDS)
    raise TimeoutError(f"server did not start: {url}")


def run_steps(scenario: dict[str, Any], out_dir: Path) -> None:
    """!
    @brief Execute the steps of a scenario in a headless browser.
    @param scenario Parsed scenario.
    @param out_dir Folder that receives the screenshots.
    """
    width, height = scenario.get("viewport", [1100, 800])
    base = scenario["base_url"]
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height})
        for step in scenario["steps"]:
            if "goto" in step:
                page.goto(base + step["goto"])
            elif "fill" in step:
                page.fill(step["fill"][0], step["fill"][1])
            elif "click" in step:
                page.click(step["click"])
                page.wait_for_load_state()
            elif "screenshot" in step:
                page.screenshot(
                    path=str(out_dir / step["screenshot"]),
                    full_page=step.get("full_page", False),
                )
                print("saved", step["screenshot"])
            else:
                raise ValueError(f"unknown step: {step}")
        browser.close()


def main() -> int:
    """!
    @brief Start services and the app, run the scenario, stop everything.
    @return Process exit code.
    """
    scenario = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)
    # The commands come from scenario files of this repository, run without a shell.
    processes = [
        subprocess.Popen(shlex.split(command))  # nosemgrep
        for command in [*scenario.get("services", []), scenario["server"]]
    ]
    try:
        wait_for(scenario["base_url"] + scenario.get("wait_path", "/"))
        run_steps(scenario, out_dir)
    finally:
        for process in processes:
            process.terminate()
    return 0


if __name__ == "__main__":
    sys.exit(main())
