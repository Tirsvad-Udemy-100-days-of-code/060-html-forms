**English** · [Dansk](Architecture-da) · [Bahasa Malaysia](Architecture-ms)

# Architecture

The code is split in layers; each layer points inward only.

- **domain**: entities (`Post`, `ContactMessage`) and errors. No Flask, no I/O.
- **application**: ports (`PostRepository`, `MailSender`) and use cases (`list_posts`, `get_post`, `send_contact_message`).
- **infrastructure**: the JSON post repository, `SmtpSettings`, `SmtpMailSender` and `UnconfiguredMailSender`.
- **presentation**: the two Flask apps, with the lecture's view names (`home`, `receive_data`, `contact`, `form_entry`).
- All constants (routes, field names, messages, ports) are in `src/html_forms/constants.py`.
