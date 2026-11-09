# SQA Review Record: PP-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [PP-001], [QC-PP-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Review of PP-001 | [56bcbfe] |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Start 2026-11-09, end 2026-11-18 and the constraint are in the Planning Assumptions and in [BC-001] Constraints |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | Five gateways, each once, with document, decision date and owner S01 |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Decision dates equal the Target Date of each MIL-* and lie inside the window |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage table maps every In Scope item to a gateway |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Chain MIL-001 to MIL-005, acyclic and in schedule order |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | A No-Go moves later dates and S01 decides on the end date |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | N-A | No governance document (GOV) exists in this project; owners and reviewers use the S-IDs of [SA-001] |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Assumptions state their source ([SA-001], lecture steps); this is the first baseline |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Three plan risks with impact and mitigation; the Udemy access risk traces to the [BC-001] risk of the same cause |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Three open issues, none contradicts the plan |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | Main deliverable column equals the Deliverable of each MIL-* |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | Stories column says "none (technical tasks)" |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Gantt dates equal the table; chain equals the dependency list |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Milestone column says "not yet synced" |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | One plan; Version History present |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | `Language` is `en` and `Domain` is `it`, no placeholders |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry domain list |
| 3 | The content (prose and table cells) is written in the stated language | Pass | Content is English throughout |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Written for the register the registry gives this type |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | The project has no dictionary (`DICT`); terms (route, form, POST, milestone, task) are used consistently, with no synonyms |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Keys, headings, IDs and statuses are English |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version, language unchanged |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The reviewer, AI as stand-in for S01, reads English and knows the IT domain, so no second language reviewer is needed (language reviewer: none) |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations (SQA, QC, PO, IT, CI) are spelled out on first use where the document uses them |

## Overall Verdict

Go — every Mandatory criterion passes, and the language and domain criteria pass. Criterion 7 is N-A because the project has no governance document. The review is not independent: the AI is author and stand-in reviewer for S01, as `process/review-checklist-process.md` allows in autonomous mode.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Challenge this stand-in review in the end-of-run summary if wanted | S01 | 2026-11-18 |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[56bcbfe]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/commit/56bcbfe9e4aee1cccad4f4802df911af9412f9de
