from ipaddress import *

ip1 = ip_address("211.115.61.154")
ip2 = ip_address("211.115.61.154")

for i in range(16, 25):
    net = ip_network(f"211.115.61.154/{i}", 0)
    if ip1 in net.hosts() and ip2 in net.hosts():
        print( net.network_address)