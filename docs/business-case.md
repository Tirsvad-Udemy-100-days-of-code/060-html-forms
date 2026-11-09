# Business Case: 060 HTML Forms

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [56bcbfe] |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted after Go review RC-001 | [56bcbfe] |

---

## Executive Summary

Day 60 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" teaches how HTML forms are submitted and how a Flask server receives the data. This project delivers the Day 60 assignment as a readable, runnable and tested Python repository: a stand-alone login form, then the blog's contact form that receives a POST and sends the site owner an email with `smtplib`. Every lecture step is documented with a screenshot in the README and explained in a wiki in English, Danish and Bahasa Malaysia.

## Methodological and Standards Foundation

The project follows the software quality assurance (SQA) and quality control (QC) framework in `framework/`: artifacts reviewed against their QC checklists, ISO/IEC 25010:2023 characteristics on every QC criterion, and a plan-first gate before code. Code follows Clean Architecture (domain, application, infrastructure, presentation), the Python conventions of the `coding-conventions` skill and the `qc-programming-python` checklist. Source is documented with Doxygen comments.

## Problem Statement

The Day 60 assignment is a chain of small challenges spread over several lectures, with solutions in gists. A participant who wants to compare solutions has no single, tested, runnable repository that shows each step, the result of each step and what was learned.

## Business Opportunity

A clear, tested repository that follows the lecture order lets fellow course participants compare their solutions and lets repository visitors learn the HTML form to Flask to email flow in one place. It also records the Product Owner's learning.

## Objectives

1. O1: Deliver the assignment's code with the assignment's function names (`home`, `login`, `receive_data`, `contact`, and so on), running on Python 3.13 or newer.
2. O2: Make the contact form work: a POST to `/contact` shows "Successfully sent your message" on the same page and sends an email to the site owner through `smtplib`.
3. O3: Cover the behaviour with automated pytest tests that need no network and no real mail server.
4. O4: Document how to create and use a local `.venv`, upgrade pip, run the app and run the tests, in a README built from the framework template.
5. O5: Show a screenshot for each lecture step in the README and explain what was gained in a wiki in English, Danish and Bahasa Malaysia.
6. O6: Publish a clear repository description and topics on the git host.

## Scope

### In Scope

- The "html-forms" demo: index page, login form, POST `/login`, `receive_data` returning the name and password as an `<h1>`.
- The blog with contact form: `/form-entry` route, the combined GET/POST `/contact` route, the Jinja `if` message in `contact.html`, and the email sent with `smtplib`.
- `pyproject.toml`, Python `.gitignore`, `constants.py`, Doxyfile, Doxygen comments, `src/`, `tests/`, `docs/`.
- README from the framework template and a three-language wiki, with screenshots per lecture step.
- Repository description and topics on the git host.

### Out of Scope

- Later bootcamp days, a database, user accounts, real authentication and password storage (the login demo only echoes the data, as the lecture does).
- Hosting or deploying the site.
- Copying Udemy video content; the repository holds the participant's own code and screenshots.
- Using or importing the personal `.env` file in the project.

## Expected Benefits

### Tangible Benefits

- A runnable repository with passing tests and one command each to run the app and the tests.
- Screenshots and a wiki for every lecture step, in three languages.

### Intangible Benefits

- Practice with HTML forms, HTTP methods, the Flask request object, Jinja conditions and `smtplib`.
- A reference other participants can compare against.

## Strategic Alignment

The project supports the Product Owner's goal of completing the 100 Days of Code bootcamp with portfolio-quality, documented work, and of applying the SQA and QC framework to personal projects.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Tests pass | 100% of tests pass on Python 3.13 | `python -m pytest` exit code 0 |
| 2 | Lecture steps covered | every task in `MIL-002` to `MIL-004` closed | closed issues on the git host |
| 3 | Screenshots | one screenshot per lecture step (L1 to L9 in `PP-001`) in README and wiki | image count against the step list |
| 4 | Wiki languages | the same page set in `en`, `da` and `ms` | `QC-WIKI` review |
| 5 | Run instructions | README steps run from a clean clone to a running app | manual run in a fresh `.venv` |
| 6 | Runtime dependencies | only Flask at runtime | `dependencies` list in `pyproject.toml` |
| 7 | Repository metadata | description and topics visible on the git host | repository page |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Email cannot be tested against a real mail server | The `smtplib` step could be wrong in production | The mail sender is behind a port; tests use a fake and a stubbed `smtplib`; the README documents the environment variables for a real run |
| Udemy lecture pages or resource zips cannot be reached from the logged-in Chrome | Starting files are missing | Rebuild the blog pages from the lecture description; record the deviation in the plan |
| Credentials leak into the repository | Security defect | `.env` is git-ignored and never imported; mail settings are read from environment variables only |
| Screenshots taken on the host desktop | Breaks the GUI testing rule | Capture in a Docker container with a headless browser (`framework/process/gui-testing.md`) |
| Course material is copyrighted | Legal or licence concern | Only the participant's own code and screenshots are published; no lecture text or video is copied |

## Assumptions

- The Product Owner is S01, who is also the developer and the reviewer; in autonomous mode the AI acts as stand-in reviewer and says so in each review record.
- The people the project is for (S02, S03) are reached only through the repository.
- The Product Owner's (PO's) language is English and the domain is information technology (IT).
- Python 3.13 or newer, Docker and `doxygen` are available on the development machine.

## Constraints

- Python 3.13 or newer, a local virtual environment (`.venv`), `pytest`, `pyproject.toml` for configuration.
- Constants live in `constants.py`.
- Folder structure `src/`, `tests/`, `docs/`.
- The only runtime dependency is Flask, because the assignment is a Flask assignment. Everything else is a development dependency.
- The personal `.env` is used from the shell only for git host calls and is never tested or imported.
- Work is done on one branch per milestone and merged by pull request.
- The project finishes by 2026-11-18, ten days after the start on 2026-11-09.

## Cost–Benefit Assessment

The assessment is qualitative on purpose: this is a personal learning project with no revenue, so a monetary return would be invented.

| Costs | Benefits |
| --- | --- |
| About 10 to 15 hours of AI-assisted work and review by S01 | A complete, tested, documented Day 60 reference in three languages |
| No licence or hosting cost | A portfolio item and a shared solution for S02 and S03 |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Wants a correct, finished assignment and a reusable workflow |
| S02 | Wants readable, runnable code with the assignment's function names and run instructions |
| S03 | Wants a clear description, topics and README, with no extra runtime dependencies |

## Recommendation

Proceed — the scope is small, the risks have mitigations and the result serves the Product Owner and both audiences.

---

[SA-001]: ./stakeholder-analysis.md
[56bcbfe]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/commit/56bcbfe9e4aee1cccad4f4802df911af9412f9de
