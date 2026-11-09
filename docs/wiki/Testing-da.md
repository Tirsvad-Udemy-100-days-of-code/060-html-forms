[English](Testing) · **Dansk** · [Bahasa Malaysia](Testing-ms)

# Test

Kør alle tests med `python -m pytest`; de bruger Flasks testklient og en falsk `MailSender`, så der er intet netværk og ingen rigtig e-mail.

- `tests/unit` dækker konstanter, indlæg samt kontaktbesked og mailindstillinger. `tests/integration` dækker begge Flask-apps.
- Stil og typer tjekkes med `ruff check .`, `ruff format --check .` og `mypy src`.
- Skærmbilleder laves i en Docker-container (`bash tools/screenshot/run.sh demo|blog|mail`), aldrig på skrivebordet.
- De samme kontroller kører i CI på hver pull request.
