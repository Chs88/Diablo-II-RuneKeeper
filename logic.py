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
        d2s_file = D2SFile(self.char_path)
        if self.is_plugy_added == True:
            d2x_file = D2XFile(self.plugy_path)
        if self.is_shared_added == True:
            sss_file = SSSFile(self.shared_path)
        print(d2s_file.char_name, d2s_file.char_level)




# class FindRunes():



