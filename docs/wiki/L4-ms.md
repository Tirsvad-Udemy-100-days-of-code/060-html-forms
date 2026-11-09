[English](L4) · [Dansk](L4-da) · **Bahasa Malaysia**

# L4 Terima data borang

## Apa yang kita peroleh

- `request.form["name"]` membaca medan yang dihantar melalui atribut `name` daripada L2.
- `receive_data()` menjawab dengan `<h1>` yang mengandungi nama dan kata laluan, seperti dalam kuliah.
- Nilai di-escape dengan `markupsafe.escape`, jadi nama seperti `<script>` tidak boleh menyuntik HTML.
- Memaparkan kata laluan hanya untuk pelajaran; aplikasi sebenar tidak pernah berbuat demikian, dan projek ini tidak pernah merekod nilai itu.

## Di mana dalam kod

- `src/html_forms/presentation/features/login/app.py` (`receive_data`)

## Tangkapan skrin

![L4 Terima data borang](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/raw/branch/main/docs/images/l4-receive-data.png)

[← L3 Hantar borang dengan POST](L3-ms) · [L5 Blog dan pautan hubungi →](L5-ms)
