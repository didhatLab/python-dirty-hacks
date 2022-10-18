import importlib
import importlib.util
import sys
import types
import os
import json


class HackPathFinder(importlib.abc.MetaPathFinder):

    def find_spec(self, fullname, path, target=None):
        if not path:
            path = [os.getcwd()]
        if "." in fullname:
            fullname = fullname.split(".")[-1]
        for cat in path:
            in_path = os.path.join(cat, fullname) + ".json"
            if os.path.exists(in_path):
                return importlib.util.spec_from_file_location(
                    name=fullname + ".json", location=in_path, loader=HackDataLoader()
                )


class HackDataLoader(importlib.abc.Loader):

    def exec_module(self, module: types.ModuleType) -> None:
        data = json.loads(open(module.__spec__.origin, "r").read())
        module.raw_data = data


sys.meta_path.append(HackPathFinder())
