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

## Installation

Open terminal inside the project folder and run:

```bash
chmod +x install.sh
./install.sh