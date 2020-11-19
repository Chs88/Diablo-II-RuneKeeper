from d2lib.files import SSSFile, D2XFile, D2SFile
from collections import Counter
import json


# if __name__ == "__main__":
#     print("Access forbidden")
# else:
#     print("soon")


class Query():
    def __init__(self, is_plugy_added, is_shared_added, char_path, plugy_path, shared_path):
        self.d2s_file = D2SFile(char_path)
        if is_plugy_added == True:
            self.d2x_file = D2XFile(plugy_path)
        if is_shared_added == True:
            self.sss_file = SSSFile(shared_path)    

    def load(self):
        instance = FindRunes()
        instance.find()




# class FindRunes():
#     def __init__(self):
#         print("test")
    
#     def find(self):
#         print("wegothere")





