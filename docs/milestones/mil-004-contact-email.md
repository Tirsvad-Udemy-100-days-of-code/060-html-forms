# Milestone 004: Contact Email

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [56bcbfe] |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted after Go review RC-007 | [56bcbfe] |

---

## Purpose

Decide whether the contact form really sends an email to the site owner, with configuration kept out of the code and the repository.

## Deliverable

A `MailSender` port, an `smtplib` adapter configured from environment variables, the use case wired into `/contact`, tests that need no network, and a screenshot of the finished form.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | A submitted contact message is passed to the mail sender with name, email, phone and message | Test passes with a fake sender | Fails |
| 2 | The `smtplib` adapter connects with TLS, logs in and sends one message, verified with a stubbed `smtplib` | Test passes | Fails |
| 3 | Mail settings come from environment variables; `.env` is not imported | No `.env` reference in `src/` | Reference found |
| 4 | A failing mail server shows an error message and does not crash the page | Test passes | Fails |
| 5 | The `qc-programming-python` review is `Go` | RC verdict Go | No-Go |
| 6 | The pytest suite passes | Exit code 0 | Fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Builds on its result |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O2, O3 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-16 — within the plan window in [PP-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Define the contact message and the MailSender port | Add a `ContactMessage` domain model and an application use case that sends it through a `MailSender` port, so the web layer does not know about `smtplib` (clean-architecture). | No |  |
| 2 | Implement the smtplib adapter | Infrastructure adapter using `smtplib.SMTP` with starttls and login, settings from environment variables named in `constants.py` (host, port, user, password, recipient). No `.env` import. | No |  |
| 3 | Wire the email into /contact (L9) | The POST branch of `contact` calls the use case and shows the success heading; on failure it shows an error. Mirrors the lecture "Sending Email with smtplib". | No |  |
| 4 | Test the email flow | Tests with a fake `MailSender` and a stubbed `smtplib`; no network and no real credentials. | No |  |
| 5 | Capture screenshots for the email step | Docker screenshots of the filled form and the success page, with a fake SMTP server, stored in `docs/images/`. | No |  |
| 6 | Review the code against qc-programming-python | Record the review as an `RC-*` before the pull request. | No |  |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[56bcbfe]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/commit/56bcbfe9e4aee1cccad4f4802df911af9412f9de
