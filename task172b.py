# %%
from pprint import pprint
import yaml


def transform_topology(filename: str):
    output = {}
    with open(filename) as file:
        data = yaml.load(file.read().replace('Eth', 'Fa'))
        for device in data:
            for key, value in zip(data[device].keys(), data[device].values()):
                output[tuple([device, key])] = tuple(list(value.items())[0])
    output_unique = output.copy()
    for key in output.keys():
        if key in output_unique.values():
            del output_unique[key]
    return output_unique


out = transform_topology("Task2_output.yaml")
pprint(out)
