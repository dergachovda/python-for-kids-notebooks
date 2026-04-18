#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if [[ ! -d ".venv" ]]; then
  if command -v python3 >/dev/null 2>&1; then
    python3 -m venv .venv
  elif command -v python >/dev/null 2>&1; then
    python -m venv .venv
  elif command -v py >/dev/null 2>&1; then
    py -3 -m venv .venv
  else
    echo "Python was not found. Install Python 3 and try again."
    exit 1
  fi
fi

if [[ -f ".venv/bin/activate" ]]; then
  # Linux/macOS style virtual environment layout.
  # shellcheck disable=SC1091
  source .venv/bin/activate
  ACTIVATE_HINT="source .venv/bin/activate"
elif [[ -f ".venv/Scripts/activate" ]]; then
  # Windows virtual environment layout used by Git Bash.
  # shellcheck disable=SC1091
  source .venv/Scripts/activate
  ACTIVATE_HINT="source .venv/Scripts/activate"
else
  echo "Could not find a virtual environment activation script in .venv"
  exit 1
fi

python -m pip install --upgrade pip
pip install -r requirements.txt

echo
echo "Workspace initialized."
echo "Environment: .venv"
echo "Activate later with: ${ACTIVATE_HINT}"
