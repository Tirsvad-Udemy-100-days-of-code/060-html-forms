# Milestone 002: HTML Forms and POST Requests

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted after Go review RC-005 | pending |

---

## Purpose

Decide whether the first half of the lecture is complete: a Flask app serves a hand-written login form that POSTs to `/login` and shows the entered data.

## Deliverable

The html-forms demo: index page with `<h1>`, login form, `login` POST route and `receive_data`, tests, and a screenshot of each lecture step.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `GET /` renders index.html containing an `<h1>` | Test passes | Fails |
| 2 | The form uses `url_for` for `action`, `method="post"` and named inputs | Test passes | Fails |
| 3 | `POST /login` returns an `<h1>` with the submitted name and password | Test passes | Fails |
| 4 | A screenshot exists for each step L1 to L4 of the lecture | All screenshots in `docs/images/` | Any missing |
| 5 | The pytest suite passes | Exit code 0 | Fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Builds on its result |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O3, O5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-12 — within the plan window in [PP-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Serve index.html with Flask | Lecture steps 1 and 2 (L1): a Flask app serving `templates/index.html` with an `<h1>`, so one can tell it works. Screenshot: the running page. | No |  |
| 2 | Build the login form in HTML | Lecture step 3 challenge (L2): a form with name and password inputs and an OK button as in the lecture picture. Screenshot: the rendered form. | No |  |
| 3 | Make the form POST to /login | Add `action` (with `url_for`) and `method="post"`, give each input a `name` attribute, and add the route accepting POST (L3). Screenshot: what happens on submit. | No |  |
| 4 | Implement receive_data | Difficult challenge (L4): read `request.form` and return the name and password as an `<h1>`. Screenshot: the result. | No |  |
| 5 | Test the html-forms demo | pytest tests with the Flask test client for GET, POST and the missing-field case. | No |  |
| 6 | Capture lecture screenshots for this milestone | Run the Docker screenshot tool for each step above and store the images in `docs/images/` for README and wiki. | No |  |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
