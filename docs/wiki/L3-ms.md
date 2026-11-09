[English](L3) · [Dansk](L3-da) · **Bahasa Malaysia**

# L3 Hantar borang dengan POST

## Apa yang kita peroleh

- `action="/login"` menyatakan ke mana pelayar menghantar data dan `method="post"` menyatakan caranya.
- GET meletakkan data dalam URL; POST meletakkannya dalam badan permintaan, jadi ia tidak dipaparkan dalam bar alamat.
- Sesebuah laluan mesti membenarkan kaedah itu: laluan `/login` hanya menerima `POST`.

## Di mana dalam kod

- `src/html_forms/presentation/features/login/templates/index.html` (the `<form>` tag)
- `src/html_forms/constants.py` (`ROUTE_LOGIN`)

## Tangkapan skrin

![L3 Hantar borang dengan POST](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/raw/branch/main/docs/images/l3-form-post.png)

[← L2 Bina borang log masuk](L2-ms) · [L4 Terima data borang →](L4-ms)
