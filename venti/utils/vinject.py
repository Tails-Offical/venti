import yaml
from venti.utils.vsys import SysInfo
import importlib

class Vinject(object):
    def __init__(self):
        self.sc = SysInfo().sys_type()
        self.oj = {}

    def yml_create(self, ij_tg):
        for i in ij_tg:
            components = i.split('.')
            module = importlib.import_module('.'.join(components[:-1]))
            class_ = getattr(module, components[-1])
            self.oj[i.split(".")[-1]] = class_

    def yml_get(self, tg):
        if "lin" in self.sc:
            folder_path = "venti/config/inject/"
        elif "win" in self.sc:
            folder_path = "venti\\config\\inject\\"
        with open(folder_path+tg, 'r') as file:
            self.config_dict = yaml.safe_load(file)
            for key, value in self.config_dict.items():
                ij_tg = value['ij']
                self.yml_create(ij_tg)
        return self.oj
