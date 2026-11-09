# Traceability Matrix: 060 HTML Forms

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [56bcbfe] |

---

## Purpose

Makes the traceability of this project measurable: which artifact instance builds on which, and when it was last reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| BC-001 | BC | en | it | - | SA-001, PP-001 | RC-001 |
| SA-001 | SA | en | it | BC-001 | PP-001 | RC-002 |
| PP-001 | PP | en | it | BC-001, SA-001 | MIL-001 to MIL-005 | RC-003 |
| MIL-001 | MIL | en | it | BC-001, PP-001 | tasks (issues) | RC-004 |
| MIL-002 | MIL | en | it | BC-001, PP-001 | tasks (issues) | RC-005 |
| MIL-003 | MIL | en | it | BC-001, PP-001 | tasks (issues) | RC-006 |
| MIL-004 | MIL | en | it | BC-001, PP-001 | tasks (issues) | RC-007 |
| MIL-005 | MIL | en | it | BC-001, PP-001 | tasks (issues) | RC-008 |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | MIL-002, MIL-003, MIL-004 | - | - | Open |
| CN-002 | MIL-001 to MIL-005 | - | - | Open |
| CN-003 | MIL-001, MIL-005 | - | - | Open |
| CN-004 | MIL-002, MIL-003 | - | - | Open |
| CN-005 | MIL-001, MIL-005 | - | - | Open |
| CN-006 | MIL-001 | - | - | Open |
| CN-007 | MIL-005 | - | - | Open |
| CN-008 | MIL-001, MIL-004 | - | - | Open |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |

## Coverage Notes

Types with no instance yet: UCD, US, UC, DM, SSD, OC, SD, DCD, ERD, TP, AD, ADR, GOV, DICT. `-` in Last Reviewed means no review record exists; in Upstream it means foundational; in Downstream it means nothing is built on it yet. The concern coverage names milestones until views exist.

---

[56bcbfe]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/commit/56bcbfe9e4aee1cccad4f4802df911af9412f9de
