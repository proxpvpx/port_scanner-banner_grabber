# Port Scanner with Banner Grabbing

A lightweight, multithreaded port scanner that identifies open ports on a target IP and attempts to capture service banners. Ideal for penetration testers and security enthusiasts aiming to map exposed services efficiently.

## Features

- Scans a customizable range of ports (default: 1-1000).
- Performs banner grabbing for detected services.
- Multithreaded for high-speed scanning.
- Gracefully handles cases where banners are unavailable.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/port-scanner.git
   cd port-scanner
   ```
Run the tool by specifying the target IP:

```
python3 port_scanner.py <IP>
```
Example:

```
python3 port_scanner.py 192.168.1.1
```
Output example:

```python
[*] Starting port scan on 192.168.1.1 (ports 1-1000)...

[+] Port 22 is open on 192.168.1.1
[+] Banner from 192.168.1.1:22 -> SSH-2.0-OpenSSH_7.9p1 Debian-10
[+] Port 80 is open on 192.168.1.1
[+] Port 443 is open on 192.168.1.1 (no banner found)

[*] Scan completed.
```
# Requirements
Python 3.6 or newer
No additional libraries required (uses Python's built-in socket module).

# Notes
Ensure you have appropriate permissions to scan the target.
For faster results, the default thread count can be adjusted in the code.

# Disclaimer
This tool is intended for educational and authorized penetration testing purposes only. Unauthorized scanning of systems is illegal and unethical. Use responsibly.
