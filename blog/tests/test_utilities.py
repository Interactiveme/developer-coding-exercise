import os

from blog.posts.business_layer.post_service import PostService
from blog.posts.data_layer.entities import PostEntity

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.blog.settings')

from django.test import TestCase
from blog.utilities.word_counter import WordCounter, stopWords


class WordCounterTestCase(TestCase):
    def setUp(self):
        self._test_string = "one two two three three three four four four four " \
                            "five five five five five six six six six six six " \
                            "be be be be be be be be be be"

    def test_top_words(self):
        counter = WordCounter(self._test_string)
        top_words = counter.top(5)
        print(self.assertEqual(5, len(top_words)))
        print(self.assertEqual('six', top_words[0]))

    def test_stop_words(self):
        words = ' '.join(stopWords)
        counter = WordCounter(words)
        top_words = counter.top(len(words))
        print(self.assertEqual(0, len(top_words)))


class EntitiesTestCase(TestCase):

    def test_get_item(self):
        title = 'I’m betting on SPAs'
        author = 'Jon Hollingsworth'
        slug = 'Im-betting-on-SPAs'

        post = PostEntity().get_item('Im-betting-on-SPAs')
        self.assertEqual(post.title, title)
        self.assertEqual(post.author, author)
        self.assertEqual(post.slug, slug)


class ServiceTestCase(TestCase):
    def test_get_all_posts(self):
        posts = PostService.get_all_posts()
        self.assertTrue(len(posts) > 0)
