# Interface to the stored data.
from abc import ABC, abstractmethod
from posts.data_layer.models import Post
from utilities.file_loader import FileLoader
from django.conf import settings


# The Entities class is a contract to program against. If the data storage mechanism is changed
# a new class can be created that implements the methods of the Entities class.
# This allows for areas of the application calling this code to remain mostly unchanged.
class Entities(ABC):
    @abstractmethod
    def get_item(self, slug):
        pass

    @abstractmethod
    def get_all_items(self):
        pass


# PostEntity is the current class that retrieves Post objects from the stored files.
class PostEntity(Entities):
    TITLE_KEY = 'Title'
    AUTHOR_KEY = 'Author'
    SLUG_KEY = 'Slug'
    METADATA_KEY = '===\n'

    def get_item(self, slug):
        post_content = self.get_file_loader().load(slug + '.md')
        if post_content is None:
            return None

        post_result = self.parse(post_content)
        return post_result

    def get_file_loader(self):
        file_loader = FileLoader(settings.POST_DIRECTORY)
        return file_loader

    def get_all_items(self):
        file_names = self.get_file_loader().file_names_in_directory()
        result = []
        for file in file_names:
            post_data = self.get_file_loader().load(file)
            post_result = self.parse(post_data)
            result.append(post_result)

        return result

    def parse(self, post_content):
        post = Post()

        meta_start = int(post_content.find(self.METADATA_KEY) + len(self.METADATA_KEY))
        meta_end = int(post_content.find(self.METADATA_KEY, meta_start)) - 1
        metadata = post_content[meta_start: meta_end].split('\n')

        metadata_dictionary = {}
        for data in metadata:
            item = data.split(': ')
            val = item[1]
            metadata_dictionary[item[0]] = val.strip()

        post.title = metadata_dictionary[self.TITLE_KEY]
        post.author = metadata_dictionary[self.AUTHOR_KEY]
        post.slug = metadata_dictionary[self.SLUG_KEY]
        post.content = post_content[meta_end + len(self.METADATA_KEY) + 1: len(post_content)]

        return post
