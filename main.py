from scanner.host_discovery import discover_hosts
from scanner.port_scanner import scan_ports
from scanner.reporter import save_json, generate_markdown


def main():
    cidr = input("Enter CIDR subnet (example 192.168.1.0/24): ")

    hosts = discover_hosts(cidr)

    results = {}

    for host in hosts:
        open_ports = scan_ports(host)
        results[host] = open_ports

    print("\n===== SCAN RESULTS =====")
    for host, ports in results.items():
        print(f"{host} -> {ports}")

    # Save repors...
    save_json(results)
    generate_markdown(results)

if __name__ == "__main__":
    main()
