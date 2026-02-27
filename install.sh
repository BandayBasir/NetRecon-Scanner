#!/bin/bash

echo "===================================="
echo "   NetRecon Scanner Installation"
echo "===================================="

if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python3 first."
    exit 1
fi

echo "[+] Creating virtual environment..."
python3 -m venv venv

echo "[+] Activating virtual environment..."
source venv/bin/activate

echo "[+] Upgrading pip..."
pip install --upgrade pip

echo "[+] Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Installation completed successfully!"
echo "Run the scanner using:"
echo "python3 main.py"
