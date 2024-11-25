import socket
import sys
from concurrent.futures import ThreadPoolExecutor

# Function to perform banner grabbing
def banner_grab(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            s.sendall(b"HEAD / HTTP/1.1\r\n\r\n")  # HTTP Banner Grabbing Example
            banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
            if banner:
                print(f"[+] Banner from {ip}:{port} -> {banner}")
            else:
                print(f"[+] Port {port} is open on {ip} (no banner found)")
    except Exception as e:
        print(f"[!] Unable to grab banner from {ip}:{port}: {e}")

# Function to scan a single port
def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((ip, port)) == 0:
                banner_grab(ip, port)
    except Exception as e:
        print(f"[!] Error scanning port {port} on {ip}: {e}")

# Main function to handle port scanning
def port_scanner(ip, start_port=1, end_port=1000):
    print(f"[*] Starting port scan on {ip} (ports {start_port}-{end_port})...\n")
    with ThreadPoolExecutor(max_workers=50) as executor:  # Use threading for faster scans
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port)
    print("\n[*] Scan completed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 port_scanner.py <IP>")
        sys.exit(1)
    
    target_ip = sys.argv[1]
    try:
        socket.inet_aton(target_ip)  # Validate IP address
        port_scanner(target_ip)
    except socket.error:
        print("[!] Invalid IP address.")
        sys.exit(1)
