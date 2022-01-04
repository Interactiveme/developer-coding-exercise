from django.db import models


# Create your models here.
class Post:

    def __init__(self):
        self.content = None
        self.slug = None
        self.author = None
        self.title = None
