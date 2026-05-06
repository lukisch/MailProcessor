@echo off
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8
set "ICON_PATH=%CD%\MailProcessor.ico"
set "PYI_TEMP=%TEMP%\MailProcessor_pyinstaller"

if exist "%PYI_TEMP%" rmdir /s /q "%PYI_TEMP%"

python -m PyInstaller ^
  --noconfirm ^
  --clean ^
  --windowed ^
  --onefile ^
  --name MailProcessor ^
  --icon "%ICON_PATH%" ^
  --add-data "resources;resources" ^
  --distpath "dist" ^
  --workpath "%PYI_TEMP%\work" ^
  --specpath "%PYI_TEMP%\spec" ^
  main.py
