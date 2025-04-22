import json
import xml.etree.ElementTree as ET
import re

class JsonParser:
    def __init__(self, filename):
        with open(filename, encoding="utf8") as tempdata:
            self.data = json.load(tempdata)

    def filter_by_values(self, **filters):
        """Filtruje dane według podanych wartości."""
        if not isinstance(self.data, list):
            return []
        return [item for item in self.data if all(item.get(key) == value for key, value in filters.items())]

    def count_by_values(self, **filters):
        """Zlicza elementy pasujące do filtrów."""
        if not isinstance(self.data, list):
            return 0
        return sum(1 for item in self.data if all(item.get(key) == value for key, value in filters.items()))

    def serialize_to_xml(self, file_path, filtered_data):
        """Konwertuje dane JSON do XML i zapisuje do pliku."""
        root = ET.Element('Data')
        
        if isinstance(filtered_data, list):
            for item in filtered_data:
                entry = ET.SubElement(root, 'Element')
                for key, value in item.items():
                    clean_key = re.sub(r'[^a-z0-9_]', '_', key.lower().strip())
                    sub_elem = ET.SubElement(entry, clean_key)
                    sub_elem.text = str(value) if value else "N/A"
        
        xml_string = ET.tostring(root, encoding='utf-8').decode('utf-8')
        
        with open(file_path, 'w', encoding='utf-8') as xml_file:
            xml_file.write(xml_string)
        print(f"XML zapisany do {file_path}")
        
        return xml_string
