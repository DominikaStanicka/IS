import yaml
import os
from jsonParser import JsonParser
from xmlParser import XmlParser

# Wczytanie konfiguracji z pliku YAML
with open(r'C:\Users\domin\Desktop\semVI\IS\z2_8\Assets\basic_config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# Wczytanie ścieżek z konfiguracji
json_file = config['paths']['json_source_file']
xml_file = config['paths']['xml_source_file']
filtered_json_file = config['paths']['json_destination_file']
filtered_xml_file = config['paths']['xml_destination_file']

# Parsowanie i filtracja JSON -> XML
json_data = JsonParser(json_file)
filtered_json = json_data.filter_by_values(Powiat='lubelski', miejscowość='Lublin')

print( filtered_json)
print("Liczba filtrowanych danych :", json_data.count_by_values(Powiat='lubelski', miejscowość='Lublin'))
json_data.serialize_to_xml(filtered_xml_file, filtered_data=filtered_json)



# Parsowanie i filtracja XML -> JSON
xml_data = XmlParser(xml_file)
print(xml_data.tags)
print(xml_data.filter_by_values(Powiat='bolesławiecki'))
print(xml_data.count_by_values(Powiat='bolesławiecki'))
xml_data.serialize_to_json(filtered_json_file, tags=['ulica', 'fax'])


