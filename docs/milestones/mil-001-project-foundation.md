# Milestone 001: Project Foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted after Go review RC-004 | pending |

---

## Purpose

Decide whether the repository is ready to receive code: tooling, documentation scaffolding, repository metadata and the screenshot tooling are in place.

## Deliverable

A repository with `pyproject.toml`, `.gitignore`, `constants.py`, the `src/` and `tests/` layout, a Doxyfile, a README from the framework template with venv instructions, a Docker screenshot tool, and a description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Python 3.13 or newer is required in `pyproject.toml` | `requires-python` is `>=3.13` | Missing or lower |
| 2 | A fresh `.venv` installs the project and `python -m pytest` passes | Exit code 0 | Fails |
| 3 | `check-readme.sh` passes on the README | Exit code 0 | Fails |
| 4 | Description and topics are visible on the git host | Both set | Either missing |
| 5 | No file from `.env` is in the repository | `git ls-files .env` is empty and `.gitignore` lists it | Tracked |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First milestone |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O4, O6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-10 — within the plan window in [PP-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create pyproject.toml | Define the project with `requires-python >=3.13`, Flask as the only runtime dependency, a `dev` extra with pytest, the `src` layout and the pytest configuration, so that `pip install -e ".[dev]"` works in a fresh `.venv`. | No |  |
| 2 | Add Python .gitignore | Ignore `.venv`, caches, build output, Doxygen output and `.env`, so no secret or generated file is committed (CN-008). | No |  |
| 3 | Create src and tests layout with constants.py | Create the `html_forms` package with layers (domain, application, infrastructure, presentation), a `constants.py` for all constants and a smoke test, following the clean-architecture folder wireframe. | No |  |
| 4 | Write README from the framework template | Build `README.md` from `framework/templates/README-template.md` with what the project is, how to create and use a local `.venv`, `python -m pip install --upgrade pip`, and how to run the app and the tests; `check-readme.sh` must pass (CN-003). | No |  |
| 5 | Add Doxyfile and Doxygen comment convention | Add a `Doxyfile` for `src/` and document the Doxygen comment style used in the source, so API docs can be generated. | No |  |
| 6 | Add Docker screenshot tool | Add a script and Dockerfile under `tools/` that start the app in a container and capture a page with a headless browser, so screenshots never use the host desktop (`framework/process/gui-testing.md`). Development tooling only, not a runtime dependency. | No |  |
| 7 | Set repository description and topics | Set a description and topics on the Gitea repository through its API with the token from `.env` used in the shell only; the file is never read by the project code (O6, CN-005). | No |  |
| 8 | Install git hooks and add CI workflow | Run `install-git-hooks.sh --enable-plan-gate` and add a CI workflow that installs the project and runs pytest, so pull requests are checked (rule 8). | No |  |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
