from ipaddress import *

def f(i):
    ip = f"{int(i):032b}"
    return ip[:16].count("0") <= ip[16:].count("0")
cnt = 0
for A in range(256)[::-1]:
    net = ip_network(f"223.167.{A}.167/255.255.255.192", 0)
    if all(f(i) for i in net):
        cnt += 1
print(cnt)