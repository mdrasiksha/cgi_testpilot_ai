@echo off
cd /d %~dp0

echo Starting Backend...

start cmd /k "cgi_testpilot_ai\backend\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000"

ping 127.0.0.1 -n 5 >nul

echo Opening Frontend...

start cgi_testpilot_ai\frontend\index.html

pause