# SQA Review Record: wiki of MIL-005

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [MIL-005], [QC-WIKI-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Wiki review for MIL-005 | pending |

---

## Artifact Under Review

- Instance reviewed: `docs/wiki/` (13 pages in English, Danish and Bahasa Malaysia, and `_Sidebar.md`)
- Checklist used: [QC-WIKI-001]
- Scope: full review
- Language and domain: en, da, ms / it
- Language reviewer: none (the AI wrote the Danish and Bahasa Malaysia text; a native read-through by S01 is welcome)
- Mode: autonomous, not independent (AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | A `_Sidebar.md` exists | Pass | docs/wiki/_Sidebar.md |
| 2 | Sidebar starts with the bold title, then one English page list, Home first | Pass | Title `Day 60: HTML forms`, 13 pages, Home first, listed once |
| 3 | Page list links every English page; no dead link | Pass | Link check over all 40 files: 0 dead links; 13 English pages all listed |
| 4 | `Related` section only when related wikis exist | Pass | No related wiki, so no such section |
| 5 | `Languages` is the last section, one line per language in that language, linking to Home | Pass | English: Home, Dansk: Hjem, Bahasa Melayu: Utama |
| 6 | Sidebar does not repeat the page list per language | Pass | One list only |
| 7 | A generated sidebar names its generator | N-A | Sidebar is hand-written, not generated |
| 9 | English plus the PO language | Pass | PO language is en; da and ms added on top |
| 10 | Page sets identical across languages | Pass | 13 pages in en, da and ms, compared by script |
| 11 | Every page starts with the language line | Pass | Current language bold, others linked to the same page |
| 12 | Non-English pages are `<Page>-<code>.md` | Pass | `-da` and `-ms` suffixes, English without suffix |
| 13 | Code, commands, file names and IDs stay English | Pass | Code blocks, file paths and identifiers are untouched in da and ms |
| 14 | Sidebar, pages and links checked on the published wiki | N-A | The publish workflow runs on merge; the published wiki is checked after the merge and reported in the end-of-run summary |
| 16 | Wiki folder is flat | Pass | All 40 files directly in docs/wiki/ |

Optional criteria 8 and 15: criterion 8 is met (every page has the language line); 15 is n/a.

## Overall Verdict

Go. Every Mandatory criterion that can be checked before the merge passes. Criterion 14 can only be checked on the published wiki after the merge; that check is an action item and its result goes into the end-of-run summary. The review is not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| After the merge, open the published wiki and check the sidebar, the three Home pages and the screenshots | AI as stand-in for S01 | 2026-11-09 |
| Read the Danish and Bahasa Malaysia text and correct wording if wanted | S01 | 2026-11-18 |

---

[MIL-005]: ../../milestones/
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
