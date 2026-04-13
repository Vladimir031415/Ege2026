from ipaddress import *

def f(ip):
    bin_ip = f"({ip}:032b)"
    return bin_ip[:8].count("0") == bin_ip[8:].count("0")

for A in range(256)[::-1]:
    net = ip_network(f"217.109,{A},94/23", False)
    if all(f(ip) for ip in net):
        print(A)