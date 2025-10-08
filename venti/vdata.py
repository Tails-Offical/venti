# -*- coding: UTF-8 -*-
import yaml
from lxml import etree

class Vdata:
    @staticmethod
    def xml_find_key(xml_data, target):
        root = etree.fromstring(xml_data) if isinstance(xml_data, str) else xml_data
        def get_xpath(element):
            path = []
            while element is not None:
                if element.getparent() is None:
                    path.append(element.tag)
                    break
                for idx, sibling in enumerate(element.getparent()):
                    if sibling is element:
                        path.append(f"{sibling.tag}[{idx + 1}]")
                        break
                element = element.getparent()
            return '/' + '/'.join(reversed(path))
        return [get_xpath(el) for el in root.xpath(f".//{target}")]

    @staticmethod
    def xml_find_value(xml_data, target):
        root = etree.fromstring(xml_data) if isinstance(xml_data, str) else xml_data
        def get_xpath(element):
            path = []
            while element is not None:
                if element.getparent() is None:
                    path.append(element.tag)
                    break
                for idx, sibling in enumerate(element.getparent()):
                    if sibling is element:
                        path.append(f"{sibling.tag}[{idx + 1}]")
                        break
                element = element.getparent()
            return '/' + '/'.join(reversed(path))
        elements_with_target_value = root.xpath(f"//*[text()='{target}']")
        return [get_xpath(el) for el in elements_with_target_value]

    @staticmethod
    def json_find_key(json_obj, key_to_find, path=""):
        paths = []
        if isinstance(json_obj, dict):
            for k, v in json_obj.items():
                new_path = f"{path}['{k}']" if path else f"['{k}']"
                if k == key_to_find:
                    paths.append(new_path)
                paths.extend(Vdata.json_find_key(v, key_to_find, new_path))
        elif isinstance(json_obj, list):
            for index, item in enumerate(json_obj):
                new_path = f"{path}[{index}]"
                paths.extend(Vdata.json_find_key(item, key_to_find, new_path))
        return paths

    @staticmethod
    def json_find_value(json_obj, value_to_find, path=""):
        paths = []
        if isinstance(json_obj, dict):
            for k, v in json_obj.items():
                new_path = f"{path}['{k}']" if path else f"['{k}']"
                if v == value_to_find:
                    paths.append(new_path)
                paths.extend(Vdata.json_find_value(v, value_to_find, new_path))
        elif isinstance(json_obj, list):
            for index, item in enumerate(json_obj):
                new_path = f"{path}[{index}]"
                paths.extend(Vdata.json_find_value(item, value_to_find, new_path))
        return paths

    @staticmethod
    def yml_write(file_path, data):
        with open(file_path, 'w') as f:
            yaml.safe_dump(data, f)

    @staticmethod
    def yml_load(file_path):
        with open(file_path, 'r') as stream:
            data = yaml.safe_load(stream)
            return data

