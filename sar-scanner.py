#!/usr/bin/env python
import time
import signal
import sys
import socket

commonly_used_port = [20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 119, 123, 137, 138, 139, 143, 161, 162, 179, 443, 445, 465, 514, 587, 636, 873, 993, 995, 1080, 1433, 1521, 1723, 1883, 2049, 3306, 3389, 5060, 5061, 5432, 5900, 5984, 6379,]
commonly_used_port2 = [20, 21, 22, 23, 25, 53, 67, 68, 80, 110,
             119, 123, 143, 161, 179, 194, 220, 389, 443, 465,
             514, 587, 636, 993, 995, 1080, 1433, 1434, 1521, 1701,
             1723, 1812, 1813, 2049, 2082, 2083, 2100, 2222, 2375, 2376,
             3128, 3306, 3389, 3690, 4333, 4444, 4440, 4505, 4506, 5432,
             5672, 5900, 5938, 5984, 6379, 6660, 6661, 6662, 6663, 6664,
             6665, 6666, 6667, 6668, 6669, 6697, 6881, 6882, 6883, 6884,
             6885, 6886, 6887, 6888, 6889, 8000, 8008, 8080, 8086, 8443,
             8888, 9000, 9042, 9060, 9080, 9100, 9200, 9300, 9418, 9443,
             9990, 11211, 27017, 27018, 27019, 28017, 37777, 44818, 47808,
             49152, 50000, 50070, 50075, 50090, 54321, 5500, 5985, 5986,
             60000, 60001, 60080, 60081, 60177, 60179, 6082, 6379, 8002, 8080, 8443, 8888, 9000, 9090, 9418, 27017, 28017]

# total_ports = list(set(commonly_used_port + commonly_used_port2))
# total_ports.sort()
# print(total_ports)
# print(len(total_ports))

name_of_ports = {
    20: "FTP Data (File Transfer Protocol)",
    21: "FTP Control (File Transfer Protocol)",
    22: "SSH (Secure Shell)",
    23: "Telnet",
    25: "SMTP (Simple Mail Transfer Protocol)",
    53: "DNS (Domain Name System)",
    67: "DHCP (Dynamic Host Configuration Protocol)",
    68: "DHCP (Dynamic Host Configuration Protocol)",
    80: "HTTP (Hypertext Transfer Protocol)",
    110: "POP3 (Post Office Protocol version 3)",
    119: "NNTP (Network News Transfer Protocol)",
    123: "NTP (Network Time Protocol)",
    137: "NetBIOS Name Service",
    138: "NetBIOS Datagram Service",
    139: "NetBIOS Session Service",
    143: "IMAP (Internet Message Access Protocol)",
    161: "SNMP (Simple Network Management Protocol)",
    162: "SNMP Trap",
    179: "BGP (Border Gateway Protocol)",
    194: "IRC (Internet Relay Chat)",
    220: "IMAP (Internet Message Access Protocol)",
    389: "LDAP (Lightweight Directory Access Protocol)",
    443: "HTTPS (Hypertext Transfer Protocol Secure)",
    445: "Microsoft-DS",
    465: "SMTPS (Simple Mail Transfer Protocol Secure)",
    514: "Syslog",
    587: "SMTP (Submission)",
    636: "LDAPS (LDAP Secure)",
    873: "Rsync",
    993: "IMAPS (Internet Message Access Protocol Secure)",
    995: "POP3S (Post Office Protocol version 3 Secure)",
    1080: "SOCKS (Socket Secure)",
    1433: "Microsoft SQL Server",
    1434: "Microsoft SQL Server",
    1521: "Oracle",
    1701: "L2TP (Layer 2 Tunneling Protocol)",
    1723: "PPTP (Point-to-Point Tunneling Protocol)",
    1812: "RADIUS (Remote Authentication Dial-In User Service)",
    1813: "RADIUS (Remote Authentication Dial-In User Service)",
    1883: "MQTT (Message Queuing Telemetry Transport)",
    2049: "NFS (Network File System)",
    2082: "cPanel",
    2083: "cPanel",
    2100: "Oracle XML DB",
    2222: "DirectAdmin",
    2375: "Docker",
    2376: "Docker (TLS)",
    3128: "Squid Proxy",
    3306: "MySQL",
    3389: "RDP (Remote Desktop Protocol)",
    3690: "SVN (Subversion)",
    4333: "mSQL",
    4440: "rsyslog",
    4444: "Metasploit",
    4505: "SaltStack",
    4506: "SaltStack",
    5060: "SIP (Session Initiation Protocol)",
    5061: "SIP (Session Initiation Protocol)",
    5432: "PostgreSQL",
    5500: "VNC (Virtual Network Computing)",
    5672: "RabbitMQ",
    5900: "VNC (Virtual Network Computing)",
    5938: "TeamViewer",
    5984: "CouchDB",
    5985: "WinRM (Windows Remote Management)",
    5986: "WinRM (Windows Remote Management)",
    6082: "Varnish Cache",
    6379: "Redis",
    6660: "IRC (Internet Relay Chat)",
    6661: "IRC (Internet Relay Chat)",
    6662: "IRC (Internet Relay Chat)",
    6663: "IRC (Internet Relay Chat)",
    6664: "IRC (Internet Relay Chat)",
    6665: "IRC (Internet Relay Chat)",
    6666: "IRC (Internet Relay Chat)",
    6667: "IRC (Internet Relay Chat)",
    6668: "IRC (Internet Relay Chat)",
    6669: "IRC (Internet Relay Chat)",
    6697: "IRC (Internet Relay Chat)",
    6881: "BitTorrent",
    6882: "BitTorrent",
    6883: "BitTorrent",
    6884: "BitTorrent",
    6885: "BitTorrent",
    6886: "BitTorrent",
    6887: "BitTorrent",
    6888: "BitTorrent",
    6889: "BitTorrent",
    8000: "HTTP Alternate",
    8002: "Teradata",
    8008: "HTTP Alternate",
    8080: "HTTP Proxy",
    8086: "InfluxDB",
    8443: "HTTPS Alternate",
    8888: "HTTP Alternate",
    9000: "SonarQube",
    9042: "Cassandra",
    9060: "WebSphere Application Server",
    9080: "WebSphere Application Server",
    9090: "WebSphere Application Server",
    9100: "JetDirect",
    9200: "Elasticsearch",
    9300: "Elasticsearch",
    9418: "Git",
    9443: "HTTPS Alternate",
    9990: "JBoss AS Management",
    11211: "Memcached",
    27017: "MongoDB",
    27018: "MongoDB",
    27019: "MongoDB",
    28017: "MongoDB",
    37777: "Dahua DVR",
    44818: "EtherNet/IP",
    47808: "BACnet",
    49152: "Windows RPC",
    50000: "SAP",
    50070: "Hadoop NameNode",
    50075: "Hadoop DataNode",
    50090: "Hadoop Secondary NameNode",
    54321: "BitTorrent",
    60000: "Deep Discovery Inspector",
    60001: "Deep Discovery Inspector",
    60080: "Deep Discovery Inspector",
    60081: "Deep Discovery Inspector",
    60177: "Freenet",
    60179: "Freenet",
    60300: "Tor (The Onion Router)",
    60389: "Tor (The Onion Router)",
    65000: "Minecraft",
    65001: "Minecraft",
    65535: "Unknown"
}

def signal_handler(sig, frame):
    print("\nsar_scanner has been closed.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


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
def show_ascii_art(art):
    for line in art.splitlines():
        print(line)
        time.sleep(0.05)

show_ascii_art(ascii_code)

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
    first_number = input("Starting from which number? ")
    last_number = input("At what number will it end? ")
    ports = list(range(int(first_number),int(last_number) + 1))

else:
    ports = list(map(int, entered_ports.split(",")))

scanning_speed = int(input("Enter the scanning centiseconds per port (1 second = 60 centisecond) (recommended: 50) ")) / 60
for port in ports:
    port_scanning(ip_address, port)

print(f"Open ports: {open_ports}\n")
print("-------INFORMATION FOR OPEN PORTS-------\n")
for i in open_ports:
    if i in open_ports:
        print(f"{i} : {name_of_ports[i]}")

input("Press enter to finish process. ")

