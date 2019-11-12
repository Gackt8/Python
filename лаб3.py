# %% 6.1
with open('ospf.txt', 'r') as f:
    print(f.read().replace('Fast', 'Gigabit'))


# %% 6.2
def task6_2(file_name):
    with open(file_name, 'r') as f:
        file = f.readlines()
    for s in file:
        if s[0] != '!':
            print(s.rstrip())


task6_2('config_sw1.txt')

# %% 6.2 a
def task6_2_a(file_name):
    ignore = ['duplex', 'alias', 'Current	configuration']
    with open(file_name, 'r') as f:
        file = f.readlines()
    for s in file:
        flag = True
        if s[0] == '!':
            flag = False
        for bw in ignore:
            if bw in s:
                flag = False
        if flag:
            print(s.rstrip())


task6_2_a('config_sw1.txt')


# %% 6.2 b
def task6_2_b(file_name):
    ignore = ['duplex', 'alias', 'Current	configuration']
    with open(file_name, 'r') as f:
        file = f.readlines()
    with open('config_sw1_cleared.txt', 'w') as f:
        f.write('')
    with open('config_sw1_cleared.txt', 'a') as f:
        for s in file:
            flag = True
            for bw in ignore:
                if bw in s:
                    flag = False
            if flag:
                f.write(s)


task6_2_b('config_sw1.txt')


# %% 6.2 c
def task6_2_c(input_file_name, output_file_name):
    ignore = ['duplex', 'alias', 'Current	configuration']
    with open(input_file_name, 'r') as f:
        file = f.readlines()
    with open(output_file_name, 'w') as f:
        f.write('')
    with open(output_file_name, 'a') as f:
        for s in file:
            flag = True
            for bw in ignore:
                if bw in s:
                    flag = False
            if flag:
                f.write(s)


task6_2_c('config_sw1.txt', 'config_sw1_cleared.txt')


# %% 6.3
with open('CAM_table.txt', 'r') as f:
    file = f.readlines()
macs = []
for i in file[6:]:
    print(i.rstrip())
    macs.append(i.split()[1])
print(macs)


# %% 6.3 a
with open('CAM_table.txt', 'r') as f:
    file = f.readlines()
file = sorted(file[6:], key=lambda e: e[1])
for i in file:
    print(i.rstrip())


# %% 6.3 b
inp_vlan = input('Vvedite VLAN id:  ')
with open('CAM_table.txt', 'r') as f:
    file = f.readlines()
for i in file[6:]:
    if inp_vlan == i.split()[0]:
        print(i.rstrip())
