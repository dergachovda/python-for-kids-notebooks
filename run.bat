@echo off
setlocal

cd /d "%~dp0"

if "%~1"=="" (
  python scripts\release.py menu
) else (
  python scripts\release.py %*
)

endlocal
