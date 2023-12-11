'''from ipaddress import *
net = ip_network('217.8.244.3/255.255.252.0', 0)
print(net)'''

'''from ipaddress import *
net = ip_network('146.212.200.55/255.255.240.0', 0) # сначала ip адресс, потом маска
for ip in net:
    if bin(int(ip)).count('0') % 2 == 0:
        k += 1
print(net)'''

'''from ipaddress import *
for mask in range(33):
    net = ip_network(f'124.128.112.142/{mask}', 0)
    print(net, net.netmask)'''

from ipaddress import *
for mask in range(33):
    net1 = ip_network(f'118.222.130.140/{mask}', 0)
    net2 = ip_network(f'118.222.201.140/{mask}', 0)
    if net1 == net2:
        print(net1, net1.netmask)