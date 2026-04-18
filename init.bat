@echo off
setlocal

cd /d "%~dp0"

if not exist ".venv" (
  py -3 -m venv .venv
)

call ".venv\Scripts\activate.bat"
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Workspace initialized.
echo Environment: .venv
echo Activate later with: .venv\Scripts\activate.bat

endlocal
