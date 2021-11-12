import socket
import subprocess
import sys
from colorama import init, Fore
from datetime import datetime

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

# Clear screen
subprocess.call('clear', shell=True)

# Ask for input
remoteServer = input('Enter a remote host to scan: ')
remoteServerIP  = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print('_'*60)
print('Please wait, scanning remote host', remoteServerIP)
print('_'*60)

# Check the date and time the scan started
t1 = datetime.now()

# Using the range function to specify ports
try:
    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print(f'{GREEN}Port {port}: \tOpen')
        sock.close()
except KeyboardInterrupt:
    print('You pressed Ctrl+C')
    sys.exit()
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()
except socket.error:
    print(f'{GRAY}Port {port}: \tClosed. Couldn\'t connect to server')
    sys.exit()

t2 = datetime.now()
total = t2 - t1
print(f'{RESET}Scanning Complete \nTime Elapsed:', total)
