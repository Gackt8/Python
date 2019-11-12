#%% 
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"

print(NAT.replace('Fast', 'Giga'))



#%%
MAC = 'AAAA:BBBB:CCCC'

print(MAC.replace(':', '.'))

#%%
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'

CONFIG = CONFIG.split(' ')
VLAN = CONFIG[4].split(',')

print(VLAN)

#%%
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

VLAN1 = command1.split(' ')
VLAN2 = command2.split(' ')

VLAN1 = VLAN1[4].split(',')
VLAN2 = VLAN2[4].split(',')

VLAN1 = set(VLAN1)
VLAN2 = set(VLAN2)

TOTAL = VLAN1 & VLAN2
TOTAL = list(TOTAL)

print(TOTAL)


#%%

VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]

VLANS = set(VLANS)
VLANS = list(VLANS)
print(VLANS)


#%%
ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.replace('O','OSPF')

RESULT = ospf_route.split(' ')

print('Protocol: ', RESULT[0])
print('Prefix: ', RESULT[1])
print('AD/Metric: ', RESULT[2])
print('Next-Hop: ', RESULT[4])
print('Last update: ', RESULT[5])
print('Outbound Interface: ', RESULT[6])

#%%

MAC = 'AAAA:BBBB:CCCC'

MAC = MAC.replace(':','')
MAC = int(MAC, 16)
MAC = bin(MAC)

print(MAC)

#%%
IP = '192.168.3.1'


NEWIP = IP.split('.')
IP = '{0:<8} {1:<8} {2:<8} {3:<7}'.format(192, 168, 3, 1)
BINIP = '{:08b} {:08b} {:08b} {:08b}'.format(192, 168, 3, 1) 
print(NEWIP)

ip_template = '''
{0:<10} {1:<10} {2:<10} {3:<10}
{0:010b} {1:010b} {2:010b} {3:010b}
'''
print(ip_template.format(192, 168, 3, 1))

print(IP)
print(BINIP)
