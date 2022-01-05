# Separate business logic from the data layer. This class gets the post records from the data layer
# and formats it before returning it to the view

import math
import markdown
from posts.data_layer.entities import PostEntity
from posts.data_transfer_objects.Posts import PostDTO, PostStubDTO
from utilities.word_counter import WordCounter
from django.utils.html import strip_tags


class PostService:
    @staticmethod
    def get_post(slug):
        post_data = PostEntity().get_item(slug)
        if post_data is None:
            return None

        content = markdown.markdown(post_data.content)
        tags = WordCounter(strip_tags(content)).top(5)
        return PostDTO(tags, content)

    @staticmethod
    def get_all_posts():
        all_posts = PostEntity().get_all_items()

        result = []
        for post in all_posts:
            content = markdown.markdown(post.content)
            end = len(content)
            end = int(math.ceil(end / 5))
            content = content[0: end]
            content = content + '...'

            stub = PostStubDTO(post.title, post.slug, post.author, content)
            result.append(stub.__dict__)

        return result
