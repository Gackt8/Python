# %% 9.1
import re

with open("sh_ip_int_br.txt") as f:
  file = f.readlines()

print("\nFa")
for line in file:
  match = re.search("Fas", line)
  if match:
    print(line, end='')
  
print("\nmanual")
for line in file:
  match = re.search("manual", line)
  if match:
    print(line, end='')

print("\nup")
for line in file:
  match = re.search("up +up", line)
  if match:
    print(line, end='')


# %% 9.1a

reg = r'Ethernet0/[13]'

file_regexp('sh_ip_int_br.txt', reg)

# %% 9.1b

reg = r'0/[13]'

file_regexp('sh_ip_int_br.txt', reg)

# %% 9.1c

reg = r'/[13]'

file_regexp('sh_ip_int_br.txt', reg)

# %% 9.2
import re


def return_match(filename, reg_e):
    with open(filename) as f:
        file = f.read()
        print(re.findall(reg_e, file))


return_match('sh_ip_int_br.txt', r'\d+\.\d+\.\d+\.\d+')

# %% 9.3
import re
from pprint import pprint


def parse_cfg(filename):
    output = []

    reg_e = r'\d+\.\d+\.\d+\.\d+ \d+\.\d+\.\d+\.\d+'

    with open(filename) as f:
        file = f.read()
    data = re.findall(reg_e, file)

    for i in data:
        output.append(tuple(i.split()))

    return output


pprint(parse_cfg('config_r1.txt'))

# %% 9.3a


def parse_cfg(filename):
    output = {}

    with open(filename) as f:
        file = f.read()
    data = re.findall(r'interface Ethernet[\s\S]*?!', file)

    for string in data:
        name = re.search(r'interface (Ethernet\d/\d)', string)[1]

        string = re.search(r'ip address (?P<ip>[\d.]{7,}) (?P<mac>[\d.]{7,})', string)

        if string:
            ip = string['ip']
            mac = string['mac']
            output[name] = (ip, mac)
        else:
            output[name] = None

    return output


pprint(parse_cfg('config_r1.txt'))

# %% 9.3b


def parse_cfg(filename):
    output = {}

    with open(filename) as f:
        file = f.read()
    data = re.findall(r'interface Ethernet[\s\S]*?!', file)

    for string in data:
        name = re.search(r'interface (Ethernet\d/\d)', string)[1]
        string = re.findall(r'ip address ([\d.]{7,}) ([\d.]{7,})', string)
        output[name] = string if string else None

    return output


pprint(parse_cfg('config_r2.txt'))