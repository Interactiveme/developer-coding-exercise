from django.db import models

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
