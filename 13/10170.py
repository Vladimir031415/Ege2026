from ipaddress import *
ip1 = ip_address("193.175.175.231")
ip2 = ip_address("193.175.176.118")

for i in range(16,25):
    net = ip_network(f"193.175.175.231/{i}", 0)
    if ip1 in net.hosts() and ip2 in net.hosts():
        print(net.network_address)
