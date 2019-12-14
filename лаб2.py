
    
# %% 7.1
from pprint import pprint
print('7.1')

access_dict = {'FastEthernet0/12': 10,
               'FastEthernet0/14': 11,
               'FastEthernet0/16': 17,
               'FastEthernet0/17': 150}


def aceess_port_congig_generation(access: dict) -> list:
    out = []

    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport	nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    for j, m in access.items():
        out.append('interface ' + j)
        for i in access_template:
            if i == access_template[1]:
                out.append(f'{i} {m}')
            else:
                out.append(i)

    return out


pprint(aceess_port_congig_generation(access_dict))

# %% 7.1a
from pprint import pprint
print('7.1a')

access_dict = {'FastEthernet0/12': 10,
               'FastEthernet0/14': 11,
               'FastEthernet0/16': 17,
               'FastEthernet0/17': 150}


def aceess_port_congig_generation(access: dict, psecurity: bool = False) -> list:
    out = []

    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport	nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']

    for j, m in access.items():
        out.append('interface ' + j)
        for i in access_template + port_security:
            if i == access_template[1]:
                out.append(f'{i} {m}')
            else:
                out.append(i)

    return out


pprint(aceess_port_congig_generation(access_dict))

# %% 7.1b
from pprint import pprint
print('7.1b')

access_dict = {'FastEthernet0/12': 10,
               'FastEthernet0/14': 11,
               'FastEthernet0/16': 17,
               'FastEthernet0/17': 150}


def aceess_port_congig_generation(access: dict, psecurity: bool = False) -> dict:
    out = dict()

    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport	nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']

    for j, m in access.items():
        out[j] = []
        out[j].append('interface ' + j)
        for i in access_template + port_security:
            if i == access_template[1]:
                out[j].append(f'{i} {m}')
            else:
                out[j].append(i)

    return out


pprint(aceess_port_congig_generation(access_dict))

# %% 7.2
print('7.2')

trunk = {'FastEthernet0/1': [10, 20],
         'FastEthernet0/2': [11, 30],
         'FastEthernet0/4': [17]}


def trunk_port_config_generator(trunk: dict) -> list:
    out = []

    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']

    for j, m in trunk.items():
        out.append('interface ' + j)
        for i in trunk_template:
            if i == trunk_template[-1]:
                out.append(f'{i} {str(m).replace("[", "").replace("]", "")}')
            else:
                out.append(i)
    return out


pprint(trunk_port_config_generator(trunk))

# %% 7.2a
print('7.2a')

trunk = {'FastEthernet0/1': [10, 20],
         'FastEthernet0/2': [11, 30],
         'FastEthernet0/4': [17]}


def trunk_port_config_generator(trunk: dict) -> dict:
    out = dict()

    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']

    for j, m in trunk.items():
        out[j] = []
        out[j].append('interface ' + j)
        for i in trunk_template:
            if i == trunk_template[-1]:
                out[j].append(f'{i} {str(m).replace("[", "").replace("]", "")}')
            else:
                out[j].append(i)
    return out


pprint(trunk_port_config_generator(trunk))


# %% 7.3
print('7.3')

def get_int_vlan_map(file_name: str) -> (dict, dict):

    access = dict()
    trunk = dict()

    with open(file_name, 'r') as f:
        file = f.read().split('!')
        #print(file)
    for i in file:
        if 'Ethernet' in i:
            #print(i)
            if 'access' in i:
                access['Fast'+i.split()[1]] = i[i.index('vlan')+1:][0]
            elif 'trunk' in i:
                i = i.split()
                trunk['Fast'+i[1]] = i[i.index('vlan')+1:][0]
    
    return access, trunk


print(get_int_vlan_map('config_sw1.txt'))

# %% 7.3a
print('7.3a')
def get_int_vlan_map(file_name: str) -> (dict, dict):

    access = dict()
    trunk = dict()

    with open(file_name, 'r') as f:
        file = f.read().split('!')
        #print(file)
    for i in file:
        if 'Ethernet' in i:
            #print(i)
            if 'access' in i:
                access['Fast'+i.split()[1]] = i[i.index('vlan')+1:][0]
            elif 'trunk' in i:
                i = i.split()
                trunk['Fast'+i[1]] = i[i.index('vlan')+1:][0]
            elif 'duplex auto' in i:
                access['Fast'+i.split()[1]] = 1
    
    return access, trunk


print(get_int_vlan_map('config_sw1.txt'))

# %% 7.4
from pprint import pprint
print('7.4')
ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command: str, ignore: list = ignore) -> bool:
    for word in ignore:
        if word in command:
            return True
    return False

def config_to_dict(config):

    text = []
    output = dict()

    with open(config) as f:
        file = f.readlines()
        for i in file:
            if not ignore_command(i) and '!' not in i and i != '\n':
                i = i.replace('\n', '')
                text.append(i)
    
    name = ''
    for i in text:
        if i[0] != ' ':
            name = i
            output[name] = []
        else:
            output[name].append(i)


    return output

pprint(config_to_dict('config_sw1.txt'))

# %% 7.4a
from pprint import pprint
print('7.4')
ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command: str, ignore: list = ignore) -> bool:
    for word in ignore:
        if word in command:
            return True
    return False

def config_to_dict(config):

    text = []
    output = dict()

    with open(config) as f:
        file = f.readlines()
        for i in file:
            if not ignore_command(i) and '!' not in i and i != '\n':
                i = i.replace('\n', '')
                text.append(i)
    
    name = ''
    second_name = ''
    for i in text:
        if i[0] != ' ':
            name = i
            output[name] = {}
        elif i[0] == ' ' and i[1] != ' ':
            second_name = i
            output[name][second_name] = []
        elif i[0] == ' ' and i[1] == ' ':
            output[name][second_name].append(i)


    return output

pprint(config_to_dict('config_sw1.txt'))