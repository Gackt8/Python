# %%
import re
import yaml


def parse_sh_cdp_neighbors(command_output: str):
    name = re.search(r"(R|SW)\d", command_output)[0]
    find = re.findall(r"((?:R|SW)\d)\s+(Eth \d/\d)[\S\d ]+(Eth \d/\d)", command_output)
    output = {name: {}}
    for f in find:
        output[name][f[1]] = {f[0]: f[2]}
    return output


def generate_topology_from_cdp(list_of_files: list, save_to_filename: str = None):
    output = {}
    for filename in list_of_files:
        with open(filename) as file:
            output.update(parse_sh_cdp_neighbors(file.read()))
    if save_to_filename is not None:
        with open(save_to_filename, "w") as file:
            yaml.dump(output, file)
    return output


files = [f"sh_cdp_n_r{i}.txt" for i in range(1, 7)] + ["sh_cdp_n_sw1.txt"]
generate_topology_from_cdp(files, "Task2_output.yaml")
