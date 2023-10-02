import socket
import sys

usage = "Python3 PORT_SCAN.py Target Start_port End_port"
print("""    
████████╗░█████╗░░█████╗░██╗░░░░░  ███████╗██╗░░██╗░█████╗░
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░  ██╔════╝██║░██╔╝██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░░░░░  █████╗░░█████═╝░███████║
░░░██║░░░██║░░██║██║░░██║██║░░░░░  ██╔══╝░░██╔═██╗░██╔══██║
░░░██║░░░╚█████╔╝╚█████╔╝███████╗  ███████╗██║░╚██╗██║░░██║
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝  ╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝
""")

if len(sys.argv) != 4:
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Host name not found!")
    sys.exit()

Start_Port = int(sys.argv[2])
End_Port = int(sys.argv[3])

for port in range(Start_Port, End_Port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # Set a timeout for the connection attempt (0.5 seconds)
    
    conn = s.connect_ex((target, port))
    
    if conn == 0:
        print("Port {} is Open".format(port))
    
    s.close()

