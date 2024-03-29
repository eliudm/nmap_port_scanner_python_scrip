#!/usr/bin/python3

import nmap 

scanner = nmap.PortScanner()

print("welcome, this is a simple automation tool")
print("<------------------------------------------>")

ip_addr =input("please enter the IP address you want to scan:")
print("The IP address you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nplease the type of scan you want to run
                1)SYN ACK scan
                2)UDP scan
                3)Comprehensive scan\n""")

print("You have selected option: ", resp) 

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS', sudo=True)
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU', sudo=True)
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['udp'].keys())

elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O', sudo=True)
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['tcp'].keys())

elif resp >= '4':
    print("Please Enter a valid option!")


