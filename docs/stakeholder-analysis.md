# Stakeholder Analysis: 060 HTML Forms

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [56bcbfe] |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted after Go review RC-002 | [56bcbfe] |

---

## Purpose

This analysis identifies the people the Day 60 repository is for and what each of them needs from it. It follows the power/interest grid and maps each concern to a FURPS+ attribute, so that the Business Case objectives and the milestones can be traced to a concern.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Finish the assignment correctly and keep a reusable, documented record of it |
| S02 | Udemy coursists | Fellow participants of the bootcamp | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | MEDIUM | Keep Informed | A clear repository description, topics and README, and no runtime dependencies beyond what is needed |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, accepts the plan and the result, and does the work.
- **Keep Informed (S02, S03):** have no say in the project but are the audience. They are served by the README, the wiki and the repository metadata, not by meetings.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The contact form must really send an email and the lecture steps must work | Functionality |
| CN-002 | S01 | Work is traceable: plan, issues, reviews and pull requests per milestone | Supportability |
| CN-003 | S02 | Code can be run from a clean clone by following the README | Usability |
| CN-004 | S02 | Function names match the assignment so solutions can be compared | Functionality |
| CN-005 | S03 | The repository explains itself: description, topics, README, screenshots | Usability |
| CN-006 | S03 | Nothing to install beyond what the assignment needs | Performance |
| CN-007 | S01 | The wiki explains what was learned in English, Danish and Bahasa Malaysia | Usability |
| CN-008 | S01 | Secrets stay out of the repository | Reliability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CR-001 | Chat with S01 | At plan acceptance and at the end of the run | Plan dry run, then run summary with each RC verdict | All |
| CR-002 | Pull request description | Per milestone | Summary and closed issues | MIL-001 to MIL-005 |
| CR-003 | README and wiki | Per milestone | Screenshots, run instructions, lessons learned | MIL-002 to MIL-005 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S03 wants no runtime dependencies, but the assignment is a Flask assignment | S01, S03 | Flask is the single runtime dependency; the blog posts are bundled data, so no HTTP client library is needed; everything else is a development dependency |
| S02 wants the assignment's function names, while Clean Architecture asks for layers | S02, S01 | The Flask view functions keep the assignment names in the presentation layer and call the application layer |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | [BC-001] O1, O2 |
| S01 | CN-002 | [BC-001] O3 |
| S02 | CN-003, CN-004 | [BC-001] O1, O4 |
| S03 | CN-005, CN-006 | [BC-001] O4, O5, O6 |
| S01 | CN-007 | [BC-001] O5 |
| S01 | CN-008 | [BC-001] O2 |

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | Pending review | |

---

[BC-001]: ./business-case.md
[56bcbfe]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/commit/56bcbfe9e4aee1cccad4f4802df911af9412f9de
