from os import listdir
from os.path import isfile, join


class FileLoader:
    def __init__(self, directory):
        self.directory = directory

    def load(self, file_name):
        if isfile(join(self.directory, file_name)):
            file = open(join(self.directory, file_name), "r")
            data = file.read()
            file.close()
            return data

        return None

    def file_names_in_directory(self):
        return [f for f in listdir(self.directory) if isfile(join(self.directory, f))]
