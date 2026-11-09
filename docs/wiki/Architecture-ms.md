[English](Architecture) · [Dansk](Architecture-da) · **Bahasa Malaysia**

# Seni bina

Kod dipecahkan kepada lapisan; setiap lapisan hanya menuju ke dalam.

- **domain**: entiti (`Post`, `ContactMessage`) dan ralat. Tiada Flask, tiada I/O.
- **application**: port (`PostRepository`, `MailSender`) dan kes guna (`list_posts`, `get_post`, `send_contact_message`).
- **infrastructure**: repositori JSON untuk catatan, `SmtpSettings`, `SmtpMailSender` dan `UnconfiguredMailSender`.
- **presentation**: dua aplikasi Flask dengan nama paparan kuliah (`home`, `receive_data`, `contact`, `form_entry`).
- Semua pemalar (laluan, nama medan, mesej, port) berada dalam `src/html_forms/constants.py`.
