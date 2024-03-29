from d2lib.files import SSSFile, D2XFile, D2SFile
from collections import Counter
import json
import results_gui as res


if __name__ == "__main__":
    print("Access forbidden") ## not necessary but fun
else:
    class FindRunes():
        def __init__(self):
            self.runes_in_inventory = []
            self.runes_in_stash = []
            self.runes_in_shared = []
            self.runes_total = []
            self.all_runewords = self.open_json()
            self.results = []

        
        def list_runes_inv(self, d2s_file):
            for item in d2s_file.items:
                if item.itype == 3 and "Rune" in item.name:## This is the most convenient way to find runes, as their type is 3 "Misc" and there is no separate type
                    self.runes_in_inventory.append(item.name[:-5])

        def list_runes_stash(self, d2x_file):
            for page in d2x_file.stash:
                for item in page['items']:
                    if item.itype == 3 and "Rune" in item.name:
                        self.runes_in_stash.append(item.name[:-5])     
        
        def list_runes_shared(self, sss_file):
            for page in sss_file.stash:
                for item in page['items']:
                    if item.itype == 3 and "Rune" in item.name:
                        self.runes_in_stash.append(item.name[:-5])


        def sum_runes(self):
            self.runes_total.extend(self.runes_in_inventory)
            self.runes_total.extend(self.runes_in_stash)
            self.runes_total.extend(self.runes_in_shared)


        def list_all(self, d2x_file): ##just a test function for code reusability
            for page in d2x_file.stash:
                for item in page['items']:
                    print(item.level)
                    print(item.name)
                    print(item.base_name)
                    print(item.magic_attrs)
            

        def open_json(self): ##opens the json for all the runewords
            with open('runewords.json', 'r') as f:
                all_runewords = json.load(f)
            return all_runewords


        def find_available_runewords(self, checklist):
            temp_counter_list = []
            runeword = checklist['runes']
            for rune in runeword:
                if rune in self.runes_total:
                    temp_counter_list.append(rune)
            if len(runeword) == len(temp_counter_list):
                self.results.append(checklist['name'])
                self.results.append(runeword)
                self.results.append(checklist['type'])
                
            
            

        def list_all_available(self):
            i = 0
            while i < len(self.all_runewords):
                self.find_available_runewords(self.all_runewords[i])
                i = i + 1