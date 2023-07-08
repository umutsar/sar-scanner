import socket

ascii_code = '''
 -----------------------------------------@utsr_---------------------------------------
/  _|      _|  _|      _|  _|      _|  _|_|_|_|_|   _|_|_|_|_|  _|_|_|_|_|  _|_|_|     /
/  _|      _|  _|_|  _|_|  _|      _|      _|       _|          _|      _|  _|    _|   /
/  _|      _|  _|  _|  _|  _|      _|      _|       _|_|_|_|_|  _|_|_|_|_|  _|_|_|_|   /
/  _|      _|  _|      _|  _|      _|      _|               _|  _|      _|  _|  _|     /
/  _|_|_|_|_|  _|      _|  _|_|_|_|_|      _|       _|_|_|_|_|  _|      _|  _|    _|   /
/                                                       _|                             /
 -----------------------------------CREATED BY UMUT SAR-------------------------------

              *************************sar_scanner*************************
'''
print(ascii_code)
print("Firstly enter target ip.")
print("Then enter port number(s) or choose one of the existing options.")
print("Finally choose number for timeout.")
open_ports = []
def port_scanning(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(scanning_speed) 
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            print(f"Port {port} open.")
            open_ports.append(port)

        else:
            print(f"Port {port} closed.")
        sock.close()
    except socket.error:
        print("Network error!")
    except:
        print("An unknown error occurred")

ip_address = input("Enter IP address: ")
commonly_used_port = [21,22,23,25,53,80,110,115,139,143,161,443,445,514,3306,3389,8080]
commonly_used_port2 = [11,12,13,21]

print(f"-Click 1 to select the most commonly used {len(commonly_used_port)} ports.")
print("-Press 2 to select commonly used ports (Level 2).")
print("-Click 3 to set the scanning range.")

entered_ports = input("Enter the numbers (separated by commas): ")
if entered_ports == "1":
    ports = commonly_used_port
    print("scanning commonly used ports...")

elif entered_ports == "2":
    ports = commonly_used_port2
    print("scanning commonly used ports(level 2)...")

elif entered_ports == "3":
    print("Select the port range (including the ones you have chosen).")
    first_number = input("Starting from which number?")
    last_number = input("At what number will it end?")
    ports = list(range(int(first_number),int(last_number) + 1))

else:
    ports = list(map(int, entered_ports.split(",")))

scanning_speed = int(input("Enter the scanning seconds per port (ex: 3): "))
for port in ports:
    port_scanning(ip_address, port)

print(f"Open ports: {open_ports}")
input("Press enter to finish process.")
