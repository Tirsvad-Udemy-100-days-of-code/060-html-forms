[English](Architecture) · **Dansk** · [Bahasa Malaysia](Architecture-ms)

# Arkitektur

Koden er delt i lag; hvert lag peger kun indad.

- **domain**: entiteter (`Post`, `ContactMessage`) og fejl. Ingen Flask, ingen I/O.
- **application**: porte (`PostRepository`, `MailSender`) og use cases (`list_posts`, `get_post`, `send_contact_message`).
- **infrastructure**: JSON-lageret for indlæg, `SmtpSettings`, `SmtpMailSender` og `UnconfiguredMailSender`.
- **presentation**: de to Flask-apps med lektionens visningsnavne (`home`, `receive_data`, `contact`, `form_entry`).
- Alle konstanter (ruter, feltnavne, beskeder, porte) ligger i `src/html_forms/constants.py`.
