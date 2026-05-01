@echo off
cd /d %~dp0

echo =====================================
echo   TestPilot AI - Auto Setup & Run
echo =====================================

REM Step 1: Check Python
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed.
    echo Please install Python 3.10+ and rerun.
    pause
    exit
)

echo Python detected

REM Step 2: Go to backend
cd cgi_testpilot_ai\backend

REM Step 3: Create venv if not exists
IF NOT EXIST .venv (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Step 4: Activate venv
call .venv\Scripts\activate

REM Step 5: Install dependencies
echo Installing dependencies...
pip install --upgrade pip >nul
pip install -r requirements.txt

REM Step 6: Start backend
echo Starting backend server...
start cmd /k "python -m uvicorn app.main:app --host 127.0.0.1 --port 8000"

cd ..

REM Step 7: Wait for backend
ping 127.0.0.1 -n 6 >nul

REM Step 8: Open frontend (FIXED)
echo Opening frontend...
start "" "%cd%\frontend\index.html"

echo =====================================
echo   App Started Successfully
echo =====================================

pause