# -*- coding: utf-8 -*-

import json

class DeserializeJson:
    # konstruktor
    def __init__(self, filename):
        print("let's deserialize something")
        with open(filename, encoding="utf8") as tempdata:
            self.data = json.load(tempdata)

    # # przykładowe statystyki
    # def somestats(self):
    #     example_stat = 0
    #     for dep in self.data:
    #         if dep['typ_JST'] == 'GM' and dep['Województwo'] == 'dolnośląskie':
    #             example_stat += 1
    #     print('liczba urzędów miejskich w województwie dolnośląskim: ' + str(example_stat))
    
    def somestats(self):
        wojewodztwa = {}  
        
        for dep in self.data:
            wojewodztwo = dep['Województwo']
            if wojewodztwo not in wojewodztwa:
                wojewodztwa[wojewodztwo] = 1  
            else:
                wojewodztwa[wojewodztwo] += 1  

        print("Liczba urzędów w poszczególnych województwach:")
        for wojewodztwo, liczba in wojewodztwa.items():
            print(f"{wojewodztwo}: {liczba}")
