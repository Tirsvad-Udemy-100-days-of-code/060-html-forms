[English](Testing) · [Dansk](Testing-da) · **Bahasa Malaysia**

# Ujian

Jalankan semua ujian dengan `python -m pytest`; ia menggunakan klien ujian Flask dan `MailSender` palsu, jadi tiada rangkaian dan tiada e-mel sebenar.

- `tests/unit` meliputi pemalar, catatan serta mesej hubungi dan tetapan mel. `tests/integration` meliputi kedua-dua aplikasi Flask.
- Gaya dan jenis disemak dengan `ruff check .`, `ruff format --check .` dan `mypy src`.
- Tangkapan skrin dibuat dalam bekas Docker (`bash tools/screenshot/run.sh demo|blog|mail`), tidak pernah di desktop.
- Semakan yang sama dijalankan dalam CI pada setiap pull request.
