#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

if [[ "$#" -eq 0 ]]; then
  python scripts/release.py menu
else
  python scripts/release.py "$@"
fi
