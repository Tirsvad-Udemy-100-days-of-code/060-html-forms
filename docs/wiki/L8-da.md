[English](L8) · **Dansk** · [Bahasa Malaysia](L8-ms)

# L8 Vis en succesbesked med Jinja

## Hvad vi har lært

- Ruten sender `msg_sent=True` til `render_template`, og `contact.html` vælger, hvad der vises.
- Jinja `{% if msg_sent %}` viser overskriften *Successfully sent your message*, ellers den normale overskrift og formularen.
- Den samme skabelon dækker derfor formularen, succes og fejl.

## Hvor det er i koden

- `src/html_forms/presentation/features/blog/templates/contact.html`
- `src/html_forms/constants.py` (`MSG_SENT_TEXT`)

## Skærmbillede

![L8 Vis en succesbesked med Jinja](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/raw/branch/main/docs/images/l8-contact-success.png)

[← L7 Én rute til GET og POST](L7-da) · [L9 Send rigtig e-mail med smtplib →](L9-da)
