# update value of each scenario from annd to 0123:0123
import os

# Get the current directory where the Python file is located
current_dir = os.path.dirname(os.path.abspath(__file__))

files_list=os.listdir(current_dir)
for txt_file in filter(lambda f: f.endswith('.txt'), files_list):

    with open(txt_file, "r",encoding='utf-8') as file:
        lines = file.readlines()

    lines[-4] = lines[-4].replace(":a", ":0:3")
    lines[-3] = lines[-3].replace(":n", ":0:2")
    lines[-2] = lines[-2].replace(":n", ":0:1")
    lines[-1] = lines[-1].replace(":d", ":3:0")

    with open(txt_file, "w", encoding="utf-8") as file:
        file.writelines(lines)

