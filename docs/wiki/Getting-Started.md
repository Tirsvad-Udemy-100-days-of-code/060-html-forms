**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

# Getting started

Requires Python 3.13 or newer. The only runtime dependency is Flask.

- Create and use a virtual environment, then install the project.
- Run the login demo (L1 to L4) and the blog (L5 to L9).

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

- Mail settings (L9) are `MAIL_HOST`, `MAIL_PORT`, `MAIL_USER`, `MAIL_PASSWORD`, `MAIL_RECIPIENT` and `MAIL_USE_TLS`; see the README for the table.
- Open the demo at <http://127.0.0.1:5000/> and the blog at <http://127.0.0.1:5001/>.
