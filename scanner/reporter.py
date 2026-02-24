import json
from datetime import datetime
import os


def save_json(results):
    """
    Save scan results into a JSON file.
    """

    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    filename = f"output/scan_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w") as file:
        json.dump(results, file, indent=4)

    print(f"\n[+] JSON report saved: {filename}")

    return filename


def generate_markdown(results):
    """
    Generate a simple markdown report.
    """

    filename = "output/report.md"

    with open(filename, "w") as file:
        file.write("# Network Scan Report\n\n")

        for host, ports in results.items():
            file.write(f"## Host: {host}\n")

            if ports:
                file.write("Open Ports:\n")
                for port in ports:
                    file.write(f"- {port}\n")
            else:
                file.write("No open ports found.\n")

            file.write("\n")

    print(f"[+] Markdown report generated: {filename}")
