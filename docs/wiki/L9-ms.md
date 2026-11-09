[English](L9) · [Dansk](L9-da) · **Bahasa Malaysia**

# L9 Hantar e-mel sebenar dengan smtplib

## Apa yang kita peroleh

- `smtplib` menghantar mesej melalui SMTP dengan STARTTLS dan log masuk.
- Penghantaran berada di sebalik port `MailSender`. Penyesuai `SmtpMailSender` melaksanakannya, dan ujian menggunakan palsu, jadi tiada e-mel sebenar dihantar semasa ujian.
- Tetapan pelayan datang daripada pemboleh ubah persekitaran `MAIL_*`; projek tidak pernah membaca fail `.env` dan tiada rahsia dalam repositori.
- Jika pelayan mel tidak dikonfigurasi atau gagal, pelawat melihat *Your message could not be sent* (HTTP 502) dan bukan kejayaan palsu.
- Tangkapan skrin dibuat dalam Docker dengan sink mel tempatan yang menerima mesej, yang membuktikan penghantaran tanpa peti mel sebenar.

## Di mana dalam kod

- `src/html_forms/application/ports/mail_sender.py`
- `src/html_forms/application/use_cases/send_contact_message.py`
- `src/html_forms/infrastructure/mail/smtp_mail_sender.py`
- `src/html_forms/infrastructure/config/mail_settings.py`

## Tangkapan skrin

![L9 Hantar e-mel sebenar dengan smtplib](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/raw/branch/main/docs/images/l9-contact-filled.png)

![L9 Hantar e-mel sebenar dengan smtplib](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/raw/branch/main/docs/images/l9-contact-sent.png)

![L9 Hantar e-mel sebenar dengan smtplib](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/raw/branch/main/docs/images/l9-inbox-after.png)

[← L8 Papar mesej berjaya dengan Jinja](L8-ms)
