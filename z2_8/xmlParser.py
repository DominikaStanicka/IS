import xml.etree.ElementTree as ET
import json

class XmlParser:
    def __init__(self, filename):
        self.tree = ET.parse(filename)
        self.root = self.tree.getroot()
        self.tags = self._get_all_tags()

    def _get_all_tags(self):
        unique_tags = set()
        for elem in self.root.iter():
            unique_tags.add(elem.tag)
        return list(unique_tags)

    def filter_by_values(self, **filters):
        list = []
        for elem in self.root.iter('Element'):
            ok = False
            for sub_elem in elem:
                if sub_elem.tag in filters.keys():
                    if sub_elem.text == filters[sub_elem.tag]:
                        ok = True
                    else:
                        continue
                else:
                    continue
            if ok:
                list.append(elem)
        return list

    def count_by_values(self, **filters):
        counter = 0
        for elem in self.root.iter('Element'):
            ok = False
            for sub_elem in elem:
                if sub_elem.tag in filters.keys():
                    if sub_elem.text == filters[sub_elem.tag]:
                        ok = True
                    else:
                        continue
                else:
                    continue
            if ok:
                counter += 1
        return counter

    def serialize_to_json(self, file_path, *tags):
        json_data = []
        for elem in self.root.iter('Element'):
            element_dict = {}
            for sub_elem in elem:
                if sub_elem.tag in tags:
                    element_dict[sub_elem.tag] = sub_elem.text.strip() if sub_elem.text else None
                else:
                    continue
            json_data.append(element_dict)
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)