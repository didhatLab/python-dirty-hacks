import os

dir_path = os.path.dirname(__file__)

for module in os.listdir(os.path.dirname(__file__)):
    if module == "kek.py":
        pth = os.path.abspath(dir_path + "/" + module)
        exec(f"import {module[:-3]}")

kek.test_func()

