@echo off
echo Killing an running versions of this script...
taskkill /F /FI "windowtitle eq Hawke.one - Trakt Sync" /T

SET mypath=%~dp0
cd %mypath%\

cls

:: Check for Python Installation
py --version 2>NUL
if errorlevel 1 goto errorNoPython

cls

title Hawke.one - Trakt Sync
color 04


py main.py
goto:eof

:errorNoPython
echo -----------------------------------------------------------------------------------
echo  Hawke.one - Trakt Sync - ERROR: Python not detected!
echo -----------------------------------------------------------------------------------
echo You will need to download and install Python to use this tool: https://www.python.org/downloads
echo Please download and install Python, then restart this tool.
echo Press any key to exit
echo.
pause > nul
