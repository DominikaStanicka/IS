# -*- coding: utf-8 -*-
"""
json to yaml converter
"""
import yaml
import json

class ConvertJsonToYaml:
    @staticmethod
    def run(data, destination_file_location):
        print("let's convert something")

        # Jeśli podano ścieżkę do pliku JSON, wczytaj go
        if isinstance(data, str):
            with open(data, 'r', encoding='utf8') as json_file:
                data = json.load(json_file)

        # Konwersja do YAML
        with open(destination_file_location, 'w', encoding='utf8') as f:
            yaml.dump(data, f, allow_unicode=True)
        
        print("it is done")
