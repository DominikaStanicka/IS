import yaml
from deserialize_json import DeserializeJson
from serialize_json import SerializeJson
from convert_json_to_yaml import ConvertJsonToYaml

# Wczytanie konfiguracji z pliku YAML
with open(r'C:\Users\domin\Desktop\semVI\IS\lab2\Assets\basic_config.yaml', encoding="utf8") as tempconffile:
    confdata = yaml.load(tempconffile, Loader=yaml.FullLoader)

# Pobranie ścieżek z konfiguracji
source_folder = confdata['paths']['source_folder']
json_source = source_folder + confdata['paths']['json_source_file']
json_destination = source_folder + confdata['paths']['json_destination_file']
yaml_destination = source_folder + confdata['paths']['yaml_destination_file']

# Pobranie ustawień operacji
source_type = confdata['options']['source_type']
operations = confdata['options']['operations']
execution_order = confdata['options']['execution_order']

# Wybór źródła (plik vs obiekt)
if source_type == "file":
    data_handler = DeserializeJson(json_source)
else:
    data_handler = DeserializeJson.from_object({"sample_key": "sample_value"})  # Przykładowy obiekt

# Wykonywanie operacji zgodnie z kolejnością
for operation in execution_order:
    if operation == "deseralizate":
        data_handler.somestats()
    elif operation == "serialize":
        SerializeJson.run(data_handler, json_destination)
    elif operation == "convert_to_yaml":
        ConvertJsonToYaml.run(json_source, yaml_destination)  # Obsługuje zarówno obiekty, jak i pliki
    else:
        print(f"Nieznana operacja: {operation}")
