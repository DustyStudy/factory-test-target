#!/usr/bin/env bash
# Gate for the issue factory: the repo's own offline tests must pass.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
python3 -m pytest -q
