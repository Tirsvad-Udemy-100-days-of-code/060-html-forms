[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

# Kom i gang

Kræver Python 3.13 eller nyere. Den eneste kørselsafhængighed er Flask.

- Opret og brug et virtuelt miljø, og installér derefter projektet.
- Kør login-demoen (L1 til L4) og bloggen (L5 til L9).

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m html_forms.presentation.features.login.app
```

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m html_forms.presentation.features.blog.app
```

- Mailindstillingerne (L9) er `MAIL_HOST`, `MAIL_PORT`, `MAIL_USER`, `MAIL_PASSWORD`, `MAIL_RECIPIENT` og `MAIL_USE_TLS`; se tabellen i README.
- Åbn demoen på <http://127.0.0.1:5000/> og bloggen på <http://127.0.0.1:5001/>.
