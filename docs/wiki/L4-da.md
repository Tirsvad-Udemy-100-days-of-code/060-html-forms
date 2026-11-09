[English](L4) · **Dansk** · [Bahasa Malaysia](L4-ms)

# L4 Modtag formulardata

## Hvad vi har lært

- `request.form["name"]` læser et indsendt felt via `name`-attributten fra L2.
- `receive_data()` svarer med en `<h1>` med navn og adgangskode, som i lektionen.
- Værdierne escapes med `markupsafe.escape`, så et navn som `<script>` ikke kan indsætte HTML.
- At vise en adgangskode er kun til øvelsen; et rigtigt program gør det aldrig, og dette projekt logger aldrig værdierne.

## Hvor det er i koden

- `src/html_forms/presentation/features/login/app.py` (`receive_data`)

## Skærmbillede

![L4 Modtag formulardata](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/raw/branch/main/docs/images/l4-receive-data.png)

[← L3 Send formularen med POST](L3-da) · [L5 Bloggen og dens kontaktlink →](L5-da)
