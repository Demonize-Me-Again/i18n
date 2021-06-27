class Translator:
    def __init__(self, files, language, split=None):
        self.files = files
        self.language = language
        self.split = '|' if split is None else split

    def get(self, path, values={}):
        keys = path.split(self.split)

        string = self.files.strings[self.language]
        
        for key in keys:
            string = string[key]

        if values:
            return string.format(**values)

        return string