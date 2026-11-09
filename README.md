# 🚀 060 HTML Forms

Day 60 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp": HTML forms, Flask POST requests and a blog contact form that really sends an email. Written for fellow course participants and for anyone browsing for ideas.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [API documentation](#-api-documentation)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The repository follows the lectures of Day 60 in order. Each step has a screenshot in this README and a page in the wiki (English, Danish and Bahasa Malaysia) that explains what it teaches.

| Part | Where | What it is |
| --- | --- | --- |
| `src/html_forms/` | source | The Flask apps, layered as domain, application, infrastructure and presentation |
| `src/html_forms/constants.py` | source | Every constant of the project, defined once |
| `tests/` | tests | `pytest` tests (unit, integration, e2e) that need no network and no mail server |
| `tools/screenshot/` | tooling | Captures the screenshots in a Docker container, never on your desktop |
| `docs/` | documents | Business case, plan, milestones, reviews and the wiki sources |

The view functions keep the names used in the assignment (`home`, `login`, `receive_data`, `contact`, ...), so solutions are easy to compare.

## 📋 Requirements

- Python 3.13 or newer.
- Flask, the only runtime dependency (installed by `pip`).
- Development only: `pytest`, `ruff` and `mypy` (installed with the `dev` extra).
- Optional: Docker, to regenerate the screenshots; Doxygen, to build the API documentation.

## 🛠️ Setup

Create a local virtual environment, upgrade pip and install the project with its development tools.

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS (bash):

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

To leave the environment, run `deactivate`.

## ▶️ Run

The commands below are added to this README as each milestone lands. Until then, the package imports and the tests run.

## 🧪 Tests

With the virtual environment active:

```bash
python -m pytest
```

Code style and types:

```bash
ruff check .
ruff format --check .
mypy src
```

## 📖 API documentation

The source uses Doxygen comments (`@file`, `@brief`, `@param`, `@return`). With Doxygen installed:

```bash
doxygen Doxyfile
```

The result is in `docs/api/html/index.html` and is not committed.

## 📄 License

GNU Affero General Public License v3, see the [LICENSE](./LICENSE) file.

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/060-html-forms/issues
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
