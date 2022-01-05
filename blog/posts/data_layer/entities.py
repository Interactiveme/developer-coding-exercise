# Interface to the stored data.
from django.utils.html import strip_tags
from abc import ABC, abstractmethod
from posts.data_layer.models import Post
from utilities.file_loader import FileLoader


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
        file_loader = FileLoader(slug + '.md')
        post_content = file_loader.load()
        if post_content is None:
            return None

        post_result = self.parse(post_content)
        return post_result

    def get_all_items(self):
        file_names = FileLoader.blog_post_file_names()
        result = []
        for file in file_names:
            file_loader = FileLoader(file)
            post_data = file_loader.load()
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
