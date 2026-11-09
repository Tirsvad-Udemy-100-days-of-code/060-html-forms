# 🚀 060 HTML Forms

Day 60 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp": HTML forms, Flask POST requests and a blog contact form that really sends an email. Written for fellow course participants and for anyone browsing for ideas.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [API documentation](#-api-documentation)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The repository follows the lectures of Day 60 in order. Each step has a screenshot in this README and a page in the wiki (English, Danish and Bahasa Malaysia) that explains what it teaches.

| Part | Where | What it is |
| --- | --- | --- |
| `src/html_forms/` | source | The Flask apps, layered as domain, application, infrastructure and presentation |
| `src/html_forms/constants.py` | source | Every constant of the project, defined once |
| `tests/` | tests | `pytest` tests (unit, integration, e2e) that need no network and no mail server |
| `tools/screenshot/` | tooling | Captures the screenshots in a Docker container, never on your desktop |
| `docs/` | documents | Business case, plan, milestones, reviews and the wiki sources |

The view functions keep the names used in the assignment (`home`, `login`, `receive_data`, `contact`, ...), so solutions are easy to compare.

## 📋 Requirements

- Python 3.13 or newer.
- Flask, the only runtime dependency (installed by `pip`).
- Development only: `pytest`, `ruff` and `mypy` (installed with the `dev` extra).
- Optional: Docker, to regenerate the screenshots; Doxygen, to build the API documentation.

## 🛠️ Setup

Create a local virtual environment, upgrade pip and install the project with its development tools.

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS (bash):

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

To leave the environment, run `deactivate`.

## ▶️ Run

With the virtual environment active, start the login form demo (lecture steps L1 to L4):

```bash
python -m html_forms.presentation.features.login.app
```

Open <http://127.0.0.1:5000/>.

Start the blog with its contact form (lecture steps L5 to L8) in a second terminal:

```bash
python -m html_forms.presentation.features.blog.app
```

Open <http://127.0.0.1:5001/>.

### Send real email from the contact form

The contact form sends the message to the site owner with `smtplib`. Configure the mail server with environment variables in the shell that starts the blog (the project never reads a `.env` file; do not commit secrets):

| Variable | Meaning | Default |
| --- | --- | --- |
| `MAIL_HOST` | SMTP server, for example `smtp.gmail.com` | required |
| `MAIL_PORT` | SMTP port | `587` |
| `MAIL_USER` | Login name, also used as the sender address | none (no login) |
| `MAIL_PASSWORD` | Password or app password | none |
| `MAIL_RECIPIENT` | Address that receives the messages | required |
| `MAIL_USE_TLS` | `false` or `0` turns STARTTLS off | `true` |

PowerShell:

```powershell
$env:MAIL_HOST = "smtp.example.com"
$env:MAIL_USER = "me@example.com"
$env:MAIL_PASSWORD = "your-app-password"
$env:MAIL_RECIPIENT = "me@example.com"
python -m html_forms.presentation.features.blog.app
```

bash:

```bash
export MAIL_HOST=smtp.example.com MAIL_USER=me@example.com MAIL_PASSWORD=your-app-password MAIL_RECIPIENT=me@example.com
python -m html_forms.presentation.features.blog.app
```

Without `MAIL_HOST` and `MAIL_RECIPIENT` the form answers "Your message could not be sent" (HTTP 502) instead of pretending to succeed.

### Lecture steps

Screenshots are captured in a Docker container (`bash tools/screenshot/run.sh demo`, `blog` or `mail`), never on your desktop.

| Step | What it shows | Screenshot |
| --- | --- | --- |
| L1 | Flask serves `index.html` with an `<h1>` | ![L1 index page][L1] |
| L2 | The hand-written login form | ![L2 login form][L2] |
| L3 | The form with `action` and `method="post"` filled in, ready to submit | ![L3 filled form][L3] |
| L4 | `receive_data` returns the name and password as an `<h1>` | ![L4 result][L4] |

| L5 | The blog home page and the contact form, which the lecture wires to a route | ![L5 blog home][L5a] ![L5 contact form][L5b] |
| L6 | `POST /form-entry` receives the form data and returns an `<h1>` | ![L6 form-entry result][L6] |
| L7 | The contact form filled in; `/contact` now handles GET and POST with `request.method` | ![L7 filled contact form][L7] |
| L8 | `contact.html` shows "Successfully sent your message" through a Jinja `if` | ![L8 success heading][L8] |
| L9 | The form sends a real email with `smtplib`; here a local mail sink in Docker received it | ![L9 filled form][L9a] ![L9 sent][L9b] ![L9 inbox][L9c] |

Notes:

- The login demo echoes the password because the lecture does; never do that in a real application.
- The Day 60 starting files could not be downloaded, so the blog is rebuilt from the lecture description with its own plain CSS (no CDN) and bundled post data.
- The lecture prints the submitted form data. This project logs only the field names and the message length, so no personal data reaches the logs.

## 🧪 Tests

With the virtual environment active:

```bash
python -m pytest
```

Code style and types:

```bash
ruff check .
ruff format --check .
mypy src
```

## 📖 API documentation

The source uses Doxygen comments (`@file`, `@brief`, `@param`, `@return`). With Doxygen installed:

```bash
doxygen Doxyfile
```

The result is in `docs/api/html/index.html` and is not committed.

## 📄 License

GNU Affero General Public License v3, see the [LICENSE](./LICENSE) file.

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/issues
[L1]: ./docs/images/l1-serve-index.png
[L2]: ./docs/images/l2-login-form.png
[L3]: ./docs/images/l3-form-post.png
[L4]: ./docs/images/l4-receive-data.png
[L5a]: ./docs/images/l5-blog-home.png
[L5b]: ./docs/images/l5-contact-form.png
[L6]: ./docs/images/l6-form-entry-result.png
[L7]: ./docs/images/l7-contact-filled.png
[L8]: ./docs/images/l8-contact-success.png
[L9a]: ./docs/images/l9-contact-filled.png
[L9b]: ./docs/images/l9-contact-sent.png
[L9c]: ./docs/images/l9-inbox-after.png
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
