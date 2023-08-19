import pyfiglet
import sys
import socket
from datetime import datetime
import concurrent.futures

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    except:
        pass

if name == "main":
    ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
    print(ascii_banner)

    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])
    else:
        print("Invalid amount of Argument")
        sys.exit(1)

    print("-" * 50)
    print("Scanning Target:", target)
    print("Scanning started at:", datetime.now())
    print("-" * 50)

    max_threads = 100  # You can adjust this value based on your system's capabilities

    with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
        futures = [executor.submit(scan_port, target, port) for port in range(1, 65536)]

    print("Scanning finished at:", datetime.now()
