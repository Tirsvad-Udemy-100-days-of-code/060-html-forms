# Headless browser image used to capture the screenshots of the lecture steps.
# Nothing here touches the host desktop (framework/process/gui-testing.md).
FROM mcr.microsoft.com/playwright/python:v1.49.0-noble

WORKDIR /work
COPY pyproject.toml README.md LICENSE ./
COPY src ./src
RUN python -m pip install --no-cache-dir .

COPY tools/screenshot /tools
ENTRYPOINT ["python", "/tools/capture.py"]
