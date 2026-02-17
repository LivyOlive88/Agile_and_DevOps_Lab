@echo off
echo ==========================================
echo   Flight Fare Analysis Pipeline - Setup
echo ==========================================

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo ==========================================
echo   Running Pipeline
echo ==========================================
python main.py

echo.
echo ==========================================
echo   Pipeline Execution Finished
echo ==========================================
pause
