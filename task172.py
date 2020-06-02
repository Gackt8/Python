# %%
import re
from pprint import pprint


def parse_sh_cdp_neighbors(command_output: str):
    name = re.search(r"(R|SW)\d", command_output)[0]
    find = re.findall(r"((?:R|SW)\d)\s+(Eth \d/\d)[\S\d ]+(Eth \d/\d)", command_output)
    output = {name: {}}
    for f in find:
        output[name][f[1]] = {f[0]: f[2]}
    return output


filenames = [f"sh_cdp_n_r{i}.txt" for i in range(1, 7)] + ["sh_cdp_n_sw1.txt"]
print(filenames)


for filename in filenames:
    with open(filename) as file:
        pprint(parse_sh_cdp_neighbors(file.read()))
