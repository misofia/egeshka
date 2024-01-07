'''from ipaddress import *
net = ip_network('217.8.244.3/255.255.252.0', 0)
print(net)'''

'''from ipaddress import *
k = 0
net = ip_network('216.130.64.0/255.255.192.0', 0) # сначала ip адресс, потом маска
for ip in net:
    if bin(int(ip)).count('0') % 2 == 0:
        k += 1
print(k)'''

'''from ipaddress import *
for mask in range(33):
    net = ip_network(f'111.7.92.52/{mask}', 0)
    print(net, net.netmask)'''

'''from ipaddress import *
for mask in range(33):
    net1 = ip_network(f'118.222.130.140/{mask}', 0)
    net2 = ip_network(f'118.222.201.140/{mask}', 0)
    if net1 == net2:
        print(net1, net1.netmask)'''

# 7007
'''from ipaddress import *
k = 0
net = ip_network('117.32.0.0/255.224.0.0', 0)
for ip in net:
    a = str(ip).split('.')
    if a.count(a[0]) + a.count(a[1]) + a.count(a[2]) + a.count(a[3]) == 6:
        k += 1
        # print(ip)
print(k - 2)'''

# 7028
'''from ipaddress import *
k = 0
net = ip_network('143.198.224.0/255.255.240.0', 0)
for ip in net:
    a = f'{ip:b}'
    if a.count(a[0]) % 2 != 0:
        k += 1
        # print(ip)
print(k)'''

# 7048
'''from ipaddress import *
k = 0
for A in range(256):
    net = ip_network(f'159.242.{A}.223/255.255.254.0', 0)
    flag = 0
    for ip in net:
        a = f'{ip:b}'
        if a[0:16].count('0') >= a[16:].count('0'):
            flag = 1
            break
    if flag == 0:
        print(A)'''
