from django.http import JsonResponse

from posts.business_layer.post_service import PostService


def post(request, slug):
    post_result = PostService.get_post(slug)
    if post_result is None:
        resp = {'post': {}}
    else:
        resp = {'post': post_result.__dict__}

    return JsonResponse(resp)


def posts(request):
    all_posts = PostService.get_all_posts()

    resp = {'posts': all_posts}
    return JsonResponse(resp)
