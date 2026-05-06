#!/usr/bin/env bash
set -euo pipefail

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --quiet notebook ipykernel
ls -a
pip -V
python -m jupyter --version
