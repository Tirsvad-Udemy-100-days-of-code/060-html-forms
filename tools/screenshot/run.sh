#!/usr/bin/env bash
# Capture the screenshots of one scenario in a Docker container.
#
# Usage: bash tools/screenshot/run.sh <scenario-name>
#   e.g. bash tools/screenshot/run.sh demo      (reads tools/screenshot/scenarios/demo.json)
# Output: docs/images/*.png
# Needs: Docker. The browser runs inside the container, not on the desktop.
set -euo pipefail

name="${1:?usage: run.sh <scenario-name>}"
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
scenario="tools/screenshot/scenarios/${name}.json"
[[ -f "${root}/${scenario}" ]] || {
	echo "no such scenario: ${scenario}" >&2
	exit 1
}

cd "${root}"
docker build -q -t html-forms-screenshot -f tools/screenshot/Dockerfile .
mkdir -p docs/images
MSYS_NO_PATHCONV=1 docker run --rm \
	-v "$(pwd -W 2>/dev/null || pwd)/docs/images:/out" \
	-v "$(pwd -W 2>/dev/null || pwd)/tools/screenshot/scenarios:/scenarios:ro" \
	html-forms-screenshot "/scenarios/${name}.json" /out
