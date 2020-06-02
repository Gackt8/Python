import re
import csv

sh_version_files = [f"sh_version_r{i}.txt" for i in range(1, 4)]
print(sh_version_files)

headers = ['hostname', 'ios', 'image', 'uptime']


# %%
def parse_sh_version(file_name: str) -> tuple:

    with open(file_name) as file:
        data_f = file.read()
        ios = re.search(r"\d{1,2}\.\d{1,2}\(\d{1,2}\)T\d*", data_f).group(0)
        image = re.search(r"(flash|disk)\S*\.(bin|T)", data_f).group(0)
        uptime = re.search(r"\d{1,2} days, \d{1,2} hours, \d{1,2} minutes", data_f).group(0)
    return ios, image, uptime


data = [headers]
for index, filename in enumerate(sh_version_files):
    row = [f"r{index}", *parse_sh_version(filename)]
    data.append(row)

print(data)

# %%
print(data)


def write_inventory_to_csv(csv_filename: str, data_: list):
    with open(csv_filename, 'w') as file:
        writer = csv.writer(file)
        for row_ in data_:
            writer.writerow(row_)


write_inventory_to_csv('Task_1.csv', data)
