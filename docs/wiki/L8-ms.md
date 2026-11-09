[English](L8) · [Dansk](L8-da) · **Bahasa Malaysia**

# L8 Papar mesej berjaya dengan Jinja

## Apa yang kita peroleh

- Laluan menghantar `msg_sent=True` kepada `render_template`, dan `contact.html` memilih apa yang dipaparkan.
- Jinja `{% if msg_sent %}` memaparkan tajuk *Successfully sent your message*, jika tidak tajuk biasa dan borang.
- Templat yang sama melayani borang, keadaan berjaya dan keadaan ralat.

## Di mana dalam kod

- `src/html_forms/presentation/features/blog/templates/contact.html`
- `src/html_forms/constants.py` (`MSG_SENT_TEXT`)

## Tangkapan skrin

![L8 Papar mesej berjaya dengan Jinja](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/raw/branch/main/docs/images/l8-contact-success.png)

[← L7 Satu laluan untuk GET dan POST](L7-ms) · [L9 Hantar e-mel sebenar dengan smtplib →](L9-ms)
