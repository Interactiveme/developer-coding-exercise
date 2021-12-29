from django.conf import settings
from os import listdir
from os.path import isfile, join

class FileLoader:
    def __init__(self, file_name):
        self.file_name = file_name

    def load(self):
        f = open(settings.POST_DIRECTORY + '/' + self.file_name, "r")
        return f.read()

    @staticmethod
    def blog_post_file_names():
        return [f for f in listdir(settings.POST_DIRECTORY) if isfile(join(settings.POST_DIRECTORY, f))]