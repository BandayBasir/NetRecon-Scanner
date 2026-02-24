@echo off
echo ==============================
echo NetRecon Scanner Installation
echo ==============================

echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Running NetRecon Scanner...
python main.py

pause