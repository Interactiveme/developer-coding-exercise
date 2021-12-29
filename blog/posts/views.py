from django.http import JsonResponse
from utilities.file_loader import FileLoader
from .models import Post, PostStub


def post(request, slug):
    file_loader = FileLoader(slug + '.md')
    post_data = file_loader.load()

    post_result = Post()
    post_result.parse(post_data)

    resp = {'data': post_result.__dict__}
    return JsonResponse(resp)


def posts(request):
    file_names = FileLoader.blog_post_file_names()
    result = []
    for file in file_names:
        file_loader = FileLoader(file)
        post_data = file_loader.load()
        post_result = PostStub().parse(post_data)
        result.append(post_result.__dict__)

    resp = {'data': result}
    return JsonResponse(resp)
