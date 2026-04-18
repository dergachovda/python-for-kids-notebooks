#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

if [[ "$#" -eq 0 ]]; then
  python3 scripts/release.py menu
else
  python3 scripts/release.py "$@"
fi
