from django.http import JsonResponse

from blog.posts.data_layer.entities import PostEntity
from blog.posts.data_layer.models import Post, PostStub


def post(request, slug):

    post_result = PostEntity().get_item(slug)
    resp = {'data': post_result.__dict__}
    return JsonResponse(resp)


def posts(request):
    post_result = PostEntity().get_all_items()

    result = []
    for post in post_result:
        stub = PostStub().parse(post_data)
        result.append(post_result.__dict__)

    resp = {'data': result}
    return JsonResponse(resp)
