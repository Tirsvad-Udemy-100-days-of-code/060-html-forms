# Headless browser image used to capture the screenshots of the lecture steps.
# Nothing here touches the host desktop (framework/process/gui-testing.md).
FROM python:3.13-slim-bookworm

ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright \
    PIP_NO_CACHE_DIR=1
RUN python -m pip install --upgrade pip \
    && python -m pip install "playwright==1.49.0" \
    && python -m playwright install --with-deps chromium \
    && useradd --create-home shooter

WORKDIR /work
COPY pyproject.toml README.md LICENSE ./
COPY src ./src
RUN python -m pip install .

COPY tools/screenshot /tools
USER shooter
ENTRYPOINT ["python", "/tools/capture.py"]
