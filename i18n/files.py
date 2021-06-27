from os import listdir
from json import load as to_json
import re, os

class Files:
    def __init__(self, path=None, file_extension=None):
        self.path = './data/translate/' if path is None else path
        self.file_extension = 'json' if file_extension is None else file_extension
        self.strings = {}
    
    def load_json(self, folder, path=None):
        path = f"{self.path}{folder}/" if path is None else path
        strings = {}
        
        for file_name in os.listdir(path):
           
           with open(f"{path}{file_name}", encoding='utf-8') as file:
               file_extension = self.file_extension
               count = - len(file_extension) - 1
               
               if self.file_extension == 'json':
                  strings[file_name[:count]] = to_json(file)
        
        self.strings[folder] = strings

    def load_folder(self, path=None, pattern=None):
        path = self.path if path is None else path

        pattern = '^[a-z]{2}((_|-)[A-Z]{2})?$' if pattern is None else pattern

        pattern = re.compile(pattern)

        for folder in [folder for folder in os.listdir(path) if pattern.match(folder)]:
            self.load_json(folder=folder, path=f"{self.path}{folder}/")