# Milestone 005: Wiki and Release

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted after Go review RC-008 | pending |

---

## Purpose

Decide whether the project is finished for its audience: README with screenshots, a wiki in three languages and a final check of the whole repository.

## Deliverable

A README with a screenshot for each lecture step, a wiki in English, Danish and Bahasa Malaysia explaining what was gained in each step, and a final verification run.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | README shows one screenshot per lecture step | Count equals the step list in `PP-001` | Any missing |
| 2 | The wiki has the same pages in `en`, `da` and `ms` | Page sets identical | A page missing |
| 3 | Each wiki page explains what was gained in its lecture step | `QC-WIKI` review is Go | No-Go |
| 4 | `_Sidebar.md` lists the English pages and the three language entries | Matches `framework/process/wiki.md` | Differs |
| 5 | From a clean clone, the README steps install, run the app and pass the tests | Verified | Fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | Builds on its result |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O4, O5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-18 — within the plan window in [PP-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the English wiki | Pages: Home, Getting Started, one page per lecture step (what we gained, screenshot), Architecture, Testing; `_Sidebar.md` as `framework/process/wiki.md` requires (CN-007). | No |  |
| 2 | Translate the wiki to Danish | Same page set as English in `*-da.md` files with the language line on each page. | No |  |
| 3 | Translate the wiki to Bahasa Malaysia | Same page set as English in `*-ms.md` files with the language line on each page. | No |  |
| 4 | Add the lecture screenshots to the README | One screenshot per lecture step with a one-line caption, in the order of the lecture (CN-005). | No |  |
| 5 | Review the wiki against QC-WIKI | Record the review as an `RC-*`. | No |  |
| 6 | Verify from a clean clone | Clone to a new folder, follow the README, run the app and the tests, and record the result in the pull request. | No |  |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
