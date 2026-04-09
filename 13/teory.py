from ipaddress import *
ip = ip_address("192.0.0.5")

net = ip_network("192.0.0.0/16", 0)

hosts = net.hosts()

broadcast_address = net.broadcast_address

network_address = net.network_address

bin_ip = f"({int(network_address):032b})"

netmask = net.netmask
