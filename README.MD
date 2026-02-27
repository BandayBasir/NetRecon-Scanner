# NetRecon Scanner

A Python-based Network Reconnaissance Tool that scans a CIDR subnet, identifies live hosts, performs port scanning, and generates structured reports.

---

## Features

- CIDR subnet scanning
- Live host discovery using ping
- TCP port scanning of common services
- JSON output of results
- Markdown report generation
- Command-line interface support

---

## How It Works

1. Accepts a CIDR subnet as input.
2. Discovers live IP addresses using ICMP ping.
3. Scans common TCP ports on active hosts.
4. Stores results in JSON format.
5. Generates a readable Markdown report.

---

## How to Run

### Windows (Recommended)

1. Clone repository:

```bash
git clone https://github.com/BandayBasir/NetRecon-Scanner.git
cd NetRecon-Scanner
```

2. Run installer:

```bash
install.bat
```

3. Enter CIDR subnet when prompted.

Example:
192.168.1.0/24

The script will automatically:
- install dependencies
- run the scanner
- generate JSON and Markdown reports

---

## Installation (Linux / macOS)

git clone https://github.com/BandayBasir/NetRecon-Scanner.git
cd NetRecon-Scanner
chmod +x install.sh
./install.sh
python3 main.py
Enter CIDR subnet when prompted.
```
