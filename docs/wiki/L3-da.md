[English](L3) · **Dansk** · [Bahasa Malaysia](L3-ms)

# L3 Send formularen med POST

## Hvad vi har lært

- `action="/login"` angiver, hvor browseren sender data, og `method="post"` angiver, hvordan.
- GET lægger data i URL'en; POST lægger dem i selve forespørgslens krop, så de ikke vises i adresselinjen.
- En rute skal tillade metoden: ruten `/login` accepterer kun `POST`.

## Hvor det er i koden

- `src/html_forms/presentation/features/login/templates/index.html` (the `<form>` tag)
- `src/html_forms/constants.py` (`ROUTE_LOGIN`)

## Skærmbillede

![L3 Send formularen med POST](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/raw/branch/main/docs/images/l3-form-post.png)

[← L2 Byg en loginformular](L2-da) · [L4 Modtag formulardata →](L4-da)
