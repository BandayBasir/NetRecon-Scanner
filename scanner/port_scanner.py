import socket

# most common industry used ports..
COMMON_PORTS = [
    21,   # FTP
    22,   # SSH
    23,   # Telnet
    25,   # SMTP
    53,   # DNS
    80,   # HTTP
    110,  # POP3
    139,  # NetBIOS
    143,  # IMAP
    443,  # HTTPS
    445,  # SMB
    3389  # RDP
]


def scan_port(ip, port):
    """
    Attempt TCP connection to check if port is open.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))
        sock.close()

        return result == 0

    except:
        return False


def scan_ports(ip):
    """
    Scan common ports on a given IP address.
    """
    print(f"\n[*] Scanning ports on {ip}")

    open_ports = []

    for port in COMMON_PORTS:
        if scan_port(ip, port):
            print(f"[+] Port {port} OPEN")
            open_ports.append(port)

    return open_ports