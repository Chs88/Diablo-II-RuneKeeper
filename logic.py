from d2lib.files import SSSFile, D2XFile, D2SFile
from collections import Counter
import json


# if __name__ == "__main__":
#     print("Access forbidden")
# else:
#     print("soon")


class Query():
    def __init__(self, is_plugy_added, is_shared_added, char_path, plugy_path, shared_path):
        self.is_plugy_added = is_plugy_added
        self.is_shared_added = is_shared_added
        self.char_path = char_path
        self.plugy_path = plugy_path
        self.shared_path = shared_path
    

    def load(self):
        print(self.is_plugy_added, self.is_shared_added, self.char_path, self.plugy_path, self.shared_path)



# class FindRunes():



