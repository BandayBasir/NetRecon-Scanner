import ipaddress
import subprocess
import platform


def ping_host(ip):
    """
    Ping a single IP address to check if it is alive.
    Works on Windows and Linux.
    """

    system = platform.system()

    if system == "Windows":
        command = ["ping", "-n", "1", "-w", "1000", str(ip)]
    else:
        command = ["ping", "-c", "1", "-W", "1", str(ip)]

    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0


def discover_hosts(cidr):
    """
    Discover live hosts inside a CIDR subnet.
    Example: 192.168.1.0/24
    """

    network = ipaddress.ip_network(cidr, strict=False)
    live_hosts = []

    print("[*] Discovering live hosts...")

    for ip in network.hosts():
        if ping_host(ip):
            print(f"[+] Host alive: {ip}")
            live_hosts.append(str(ip))

    return live_hosts