[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Malaysia**

# Bermula

Memerlukan Python 3.13 atau lebih baharu. Satu-satunya kebergantungan masa jalan ialah Flask.

- Cipta dan gunakan persekitaran maya, kemudian pasang projek.
- Jalankan demo log masuk (L1 hingga L4) dan blog (L5 hingga L9).

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

- Tetapan mel (L9) ialah `MAIL_HOST`, `MAIL_PORT`, `MAIL_USER`, `MAIL_PASSWORD`, `MAIL_RECIPIENT` dan `MAIL_USE_TLS`; lihat jadual dalam README.
- Buka demo di <http://127.0.0.1:5000/> dan blog di <http://127.0.0.1:5001/>.
