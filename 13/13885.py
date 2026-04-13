from ipaddress import *

def f(ip):
    bin_ip = f"({ip}:032b)"
    return bin_ip[:8].count("1") == bin_ip[8:].count("1")

for A in range(9)[::-1]:
    net = ip_network(f"238, 51, 1, 202/{16+A}", False)
    if all(f(ip) for ip in net):
        print(A)