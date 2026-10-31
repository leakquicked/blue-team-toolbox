![Python checks](https://github.com/leakquicked/blue-team-toolbox/actions/workflows/python-checks.yml/badge.svg)

# Blue Team Toolbox

Offline text triage helpers for blue-team learning.

## Usage
```bash
python blue_team_toolbox.py sample.txt
python blue_team_toolbox.py sample.txt --output report.json
```

Python 3.10+, standard library only. The tool reads a local UTF-8 text file and emits JSON findings. It makes no network requests and does not modify input files.

## Rules
- `encoded` — medium severity heuristic.
- `evasion` — high severity heuristic.

Findings are leads for human review, not proof of compromise. Use only data you own or are authorized to inspect. Do not publish personal or confidential data.

## Tests
Run `python -m unittest discover -s tests -v`.
