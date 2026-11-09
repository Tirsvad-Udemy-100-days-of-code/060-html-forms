[English](L7) · [Dansk](L7-da) · **Bahasa Malaysia**

# L7 Satu laluan untuk GET dan POST

## Apa yang kita peroleh

- Satu laluan, `/contact`, boleh menghidangkan borang kosong (GET) dan borang yang dihantar (POST).
- Paparan menyemak `request.method` dan bercabang, yang menghapuskan URL kedua.
- Teks yang dihantar disahkan oleh entiti `ContactMessage`: medan dipangkas, baris baru dalam pengirim atau subjek ditolak dan mesej kosong tidak diterima.

## Di mana dalam kod

- `src/html_forms/presentation/features/blog/app.py` (`BlogViews.contact`)
- `src/html_forms/domain/entities/contact_message.py`

## Tangkapan skrin

![L7 Satu laluan untuk GET dan POST](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/raw/branch/main/docs/images/l7-contact-filled.png)

[← L6 Laluan form-entry](L6-ms) · [L8 Papar mesej berjaya dengan Jinja →](L8-ms)
