#!/usr/bin/env bash
# Gate for the issue factory: the repo's own offline tests must pass.
# Runners' system Python is externally managed and has no pytest, so install the
# pinned test dependency into a throwaway venv.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

venv="$(mktemp -d)/venv"
python3 -m venv "$venv"
"$venv/bin/pip" install --quiet "pytest==9.1.1"
"$venv/bin/python" -m pytest -q
