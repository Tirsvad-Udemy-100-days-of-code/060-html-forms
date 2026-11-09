[English](L9) · **Dansk** · [Bahasa Malaysia](L9-ms)

# L9 Send rigtig e-mail med smtplib

## Hvad vi har lært

- `smtplib` sender beskeden over SMTP med STARTTLS og login.
- Afsendelsen ligger bag en `MailSender`-port. Adapteren `SmtpMailSender` implementerer den, og test bruger en attrap, så der ikke sendes rigtig e-mail under test.
- Serverindstillingerne kommer fra `MAIL_*`-miljøvariabler; projektet læser aldrig en `.env`-fil, og ingen hemmeligheder ligger i repositoriet.
- Hvis mailserveren ikke er sat op eller fejler, ser den besøgende *Your message could not be sent* (HTTP 502) i stedet for en falsk succes.
- Skærmbillederne blev lavet i Docker med en lokal mail-sink, der modtog beskeden, hvilket beviser leveringen uden en rigtig postkasse.

## Hvor det er i koden

- `src/html_forms/application/ports/mail_sender.py`
- `src/html_forms/application/use_cases/send_contact_message.py`
- `src/html_forms/infrastructure/mail/smtp_mail_sender.py`
- `src/html_forms/infrastructure/config/mail_settings.py`

## Skærmbilleder

![L9 Send rigtig e-mail med smtplib](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/raw/branch/main/docs/images/l9-contact-filled.png)

![L9 Send rigtig e-mail med smtplib](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/raw/branch/main/docs/images/l9-contact-sent.png)

![L9 Send rigtig e-mail med smtplib](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/raw/branch/main/docs/images/l9-inbox-after.png)

[← L8 Vis en succesbesked med Jinja](L8-da)
