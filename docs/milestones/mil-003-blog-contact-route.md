# Milestone 003: Blog Contact Route

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted after Go review RC-006 | pending |

---

## Purpose

Decide whether the blog runs and its contact form is wired to a single `/contact` route that handles GET and POST.

## Deliverable

The Bootstrap blog (home, about, post, contact), a `/form-entry` route, the combined `/contact` GET/POST route and the Jinja message, with tests and screenshots.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Home, about, post and contact pages render | Tests pass | Fails |
| 2 | `POST /form-entry` prints the form data and returns "Successfully sent your message" | Test passes | Fails |
| 3 | `/contact` handles GET and POST using `request.method` | Tests pass | Fails |
| 4 | `contact.html` shows the success `<h1>` through a Jinja `if` | Test passes | Fails |
| 5 | A screenshot exists for each step L5 to L8 of the lecture | All in `docs/images/` | Any missing |
| 6 | The blog posts are bundled data, no HTTP client dependency | `pyproject.toml` lists Flask only | Another runtime dependency |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Builds on its result |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O2, O3, O5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-14 — within the plan window in [PP-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set up the blog from the Day 60 starting files (L5) | Get the starting files from the course resource (download from Udemy through the logged-in Chrome, once the user has accepted this plan), or rebuild them from the lecture; serve home, about, post and contact pages with bundled post data. Screenshot: home and contact pages. | No |  |
| 2 | Add the /form-entry route | Lecture step 2 (L5): receive the form POST in `/form-entry`. Screenshot of the form. | No |  |
| 3 | Print the form data and return the success heading | Challenge 3 (L6): print name, email, phone and message and return an `<h1>` "Successfully sent your message". Screenshot of the result. | No |  |
| 4 | Combine /contact and /form-entry | Challenge 4 (L7): one `/contact` route for GET and POST, deciding with `request.method`; update the form action. Screenshot of the result. | No |  |
| 5 | Show the success heading with Jinja | Challenge 5 (L8): render the heading in `contact.html` with a Jinja `if`, instead of returning a string. Screenshot of the result. | No |  |
| 6 | Test the blog routes and capture screenshots | pytest tests for each route and method, and Docker screenshots for the steps above in `docs/images/`. | No |  |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
