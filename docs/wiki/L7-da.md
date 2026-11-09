[English](L7) · **Dansk** · [Bahasa Malaysia](L7-ms)

# L7 Én rute til GET og POST

## Hvad vi har lært

- Én rute, `/contact`, kan både vise den tomme formular (GET) og den indsendte formular (POST).
- Visningen tjekker `request.method` og forgrener sig, hvilket fjerner den anden URL.
- Den indsendte tekst valideres af entiteten `ContactMessage`: felter trimmes, linjeskift i afsender eller emne afvises, og en tom besked nægtes.

## Hvor det er i koden

- `src/html_forms/presentation/features/blog/app.py` (`BlogViews.contact`)
- `src/html_forms/domain/entities/contact_message.py`

## Skærmbillede

![L7 Én rute til GET og POST](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/raw/branch/main/docs/images/l7-contact-filled.png)

[← L6 Ruten form-entry](L6-da) · [L8 Vis en succesbesked med Jinja →](L8-da)
