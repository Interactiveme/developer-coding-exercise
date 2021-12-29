from django.db import models
from django.utils.html import strip_tags
from utilities.markdown_stripper import unmark
from utilities.word_counter import WordCounter
import math

# Create your models here.
class Post:
    TITLE_KEY = 'Title:'
    AUTHOR_KEY = 'Author:'
    SLUG_KEY = 'Slug:'
    METADATA_KEY = '===\n'

    def __init__(self):
        self.tags = None
        self.content = None
        self.slug = None
        self.author = None
        self.title = None

    def parse(self, post_content):
        meta_start = int(post_content.find(self.METADATA_KEY) + len(self.METADATA_KEY))
        meta_end = int(post_content.find(self.METADATA_KEY, meta_start)) - 1
        metadata = post_content[meta_start: meta_end].split('\n')

        self.title = strip_tags(metadata[0][metadata[0].find(':') + 1: len(metadata[0])].strip())
        self.author = strip_tags(metadata[1][metadata[1].find(':') + 1: len(metadata[1])].strip())
        self.slug = strip_tags(metadata[2][metadata[2].find(':') + 1: len(metadata[2])].strip())
        content = post_content[meta_end + len(self.METADATA_KEY) + 1: len(post_content)] \
            .replace('\n', ' ') \
            .replace('  ', ' ')

        content = unmark(content)
        self.tags = WordCounter(content).top(5)
        self.content = content
        return self


class PostStub(Post):
    def __init__(self):
        super(PostStub, self).__init__()

    def parse(self, post_content):
        super(PostStub, self).parse(post_content)

        end = len(self.content)
        print(end)
        end = int(math.ceil(end / 3))
        print(end)
        self.content = self.content[0: end]
        self.content = self.content + '...'

        return self
