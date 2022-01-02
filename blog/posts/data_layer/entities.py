from django.utils.html import strip_tags
from abc import ABC, abstractmethod

from blog.posts.data_layer.models import Post, PostStub
from blog.utilities.markdown_stripper import unmark
from blog.utilities.word_counter import WordCounter
from blog.utilities.file_loader import FileLoader


class Entities(ABC):
    @abstractmethod
    def get_item(self, slug):
        ...

    @abstractmethod
    def get_all_items(self):
        ...


class PostEntity(Entities):
    def get_item(self, slug):
        file_loader = FileLoader(slug + '.md')
        post_content = file_loader.load()
        post_result = self.parse(post_content)

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

        post.title = strip_tags(metadata[0][metadata[0].find(':') + 1: len(metadata[0])].strip())
        post.author = strip_tags(metadata[1][metadata[1].find(':') + 1: len(metadata[1])].strip())
        post.slug = strip_tags(metadata[2][metadata[2].find(':') + 1: len(metadata[2])].strip())
        content = post_content[meta_end + len(self.METADATA_KEY) + 1: len(post_content)] \
            .replace('\n', ' ') \
            .replace('  ', ' ')

        content = unmark(content)
        post.tags = WordCounter(content).top(5)
        post.content = content
        return post
