from d2lib.files import SSSFile, D2XFile, D2SFile
from collections import Counter
import json


if __name__ == "__main__":
    print("Access forbidden")
else:
    class Query():
        def __init__(self, is_plugy_added, is_shared_added, char_path, plugy_path, shared_path):
            self.is_plugy_added = is_plugy_added
            self.is_shared_added = is_shared_added
            self.d2s_file = D2SFile(char_path)
            self.d2x_file = None
            self.sss_file = None
            if is_plugy_added == True:
                self.d2x_file = D2XFile(plugy_path)
                self.sss_file = None
            if is_shared_added == True:
                self.d2x_file = D2XFile(plugy_path)
                self.sss_file = SSSFile(shared_path)    

        def start(self):
            instance = FindRunes()
            instance.list_runes_inv(self.d2s_file)
            if (self.is_plugy_added == True) and (self.is_shared_added == False):
                instance.list_runes_stash(self.d2x_file)
            elif (self.is_plugy_added == True) and (self.is_shared_added == True):
                instance.list_runes_stash(self.d2x_file)
                instance.list_runes_shared(self.sss_file)
            instance.sum_runes()
            print(instance.runes_total)


    class FindRunes():
        def __init__(self):
            self.runes_in_inventory = []
            self.runes_in_stash = []
            self.runes_in_shared = []
            self.runes_total = []

        
        def list_runes_inv(self, d2s_file):
            for item in d2s_file.items:
                if item.itype == 3 and "Rune" in item.name:
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


        def list_all(self, d2x_file):
            for page in d2x_file.stash:
                for item in page['items']:
                    print(item.level)
                    print(item.name)
                    print(item.base_name)
                    print(item.magic_attrs)
            

        def open_json(self):
            with open('runewords.json', 'r') as f:
                all_runewords = json.load(f)
            return all_runewords


