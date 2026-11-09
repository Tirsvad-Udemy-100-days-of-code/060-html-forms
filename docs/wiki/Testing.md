**English** · [Dansk](Testing-da) · [Bahasa Malaysia](Testing-ms)

# Testing

Run all tests with `python -m pytest`; they use Flask's test client and a fake `MailSender`, so no network and no real email.

- `tests/unit` covers constants, posts and the contact message and mail settings. `tests/integration` covers both Flask apps.
- Style and types are checked with `ruff check .`, `ruff format --check .` and `mypy src`.
- Screenshots are made in a Docker container (`bash tools/screenshot/run.sh demo|blog|mail`), never on the desktop.
- The same checks run in CI on every pull request.
