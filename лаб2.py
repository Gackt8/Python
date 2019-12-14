# %% 5.1
ip = input('Р’РІРµРґРёС‚Рµ IP: ')
ip1 = int(ip.split('.')[0])
if 1 <= ip1 <= 127:
    print('unicast (class A)')
elif 128 <= ip1 <= 191:
    print('unicast (class B)')
elif 192 <= ip1 <= 223:
    print('unicast (class C)')
elif 224 <= ip1 <= 239:
    print('multicast (class D)')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')

# %% 5.1a
flag = True
ip = input('Р’РІРµРґРёС‚Рµ IP: ')
if ip.count('.') != 3:
    flag = False
if flag:
    for i in ip.split('.'):
        if not i.isdigit():
            flag = False
if flag:
    for i in ip.split('.'):
        if not 0 <= int(i) <= 255:
            flag = False

if flag:
    ip1 = int(ip.split('.')[0])
    if 1 <= ip1 <= 127:
        print('unicast (class A)')
    elif 128 <= ip1 <= 191:
        print('unicast (class B)')
    elif 192 <= ip1 <= 223:
        print('unicast (class C)')
    elif 224 <= ip1 <= 239:
        print('multicast (class D)')
    elif ip == '255.255.255.255':
        print('local broadcast')
    elif ip == '0.0.0.0':
        print('unassigned')
    else:
        print('unused')
else:
    print('Incorrect	IPv4	address')

# %% 5.1b
flag = True
while 1:
    ip = input('Р’РІРµРґРёС‚Рµ IP: ')
    if ip.count('.') != 3:
        flag = False
    if flag:
        for i in ip.split('.'):
            if not i.isdigit():
                flag = False
    if flag:
        for i in ip.split('.'):
            if not 0 <= int(i) <= 255:
                flag = False
    if flag:
        break
    else:
        print('Incorrect	IPv4	address')
        print('Try again or press Ctrl + C for EXIT')

ip1 = int(ip.split('.')[0])
if 1 <= ip1 <= 127:
    print('unicast (class A)')
elif 128 <= ip1 <= 191:
    print('unicast (class B)')
elif 192 <= ip1 <= 223:
    print('unicast (class C)')
elif 224 <= ip1 <= 239:
    print('multicast (class D)')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')

# %% 5.1c
while True:
    ip = input('Р’РІРµРґРёС‚Рµ IP: ')

    if ip.count('.') == 3 \
            and all([i.isdigit() for i in ip.split('.')]) \
            and all([0 <= int(i) <= 255 for i in ip.split('.')]):
        break
    else:
        print('Incorrect	IPv4	address')
        print('Try again or press Ctrl + C for EXIT')

ip1 = int(ip.split('.')[0])
if 1 <= ip1 <= 127:
    print('unicast (class A)')
elif 128 <= ip1 <= 191:
    print('unicast (class B)')
elif 192 <= ip1 <= 223:
    print('unicast (class C)')
elif 224 <= ip1 <= 239:
    print('multicast (class D)')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')

# %% 5.2
mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
print(mac)
mac_cisco = [i.replace(':', '.') for i in mac]
print(mac_cisco)

# %% 5.3
access_template = ['switchport mode access', 'switchport access vlan', 'spanning-tree portfast',
                   'spanning-tree bpduguard enable']
trunk_template = ['switchport trunk encapsulation dot1q', 'switchport mode trunk', 'switchport trunk allowed vlan']
fast_int = {'access': {'0/12': '10', '0/14': '11', '0/16': '17', '0/17': '150'},
            'trunk': {'0/1': ['add', '10', '20'], '0/2': ['only', '11', '30'], '0/4': ['del', '17']}}

for intf, vlan in fast_int['access'].items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print('	{}	{}'.format(command, vlan))
        else:
            print('	{}'.format(command))

for intf, val in fast_int['trunk'].items():
    print('interface FastEthernet' + intf)
    for com in trunk_template:
        if not com.endswith('vlan'):
            print(' ' * 7, com)
        else:
            if val[0] == 'add':
                print(' ' * 7, com, 'add', ','.join(val[1:]))
            elif val[0] == 'only':
                print(' ' * 7, com, 'remove', ','.join(val[1:]))
            elif val[0] == 'del':
                print(' ' * 7, com, ','.join(val[1:]))