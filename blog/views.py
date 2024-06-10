from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader

from blog.models import Post, Comment


def index(request, *args, **kwargs):
    post_id = request.GET.get("post_id", 1)
    post = Post.objects.get(pk=post_id)

    context = {
        "test_post": post
    }
    template = loader.get_template('blog/index.html')

    return HttpResponse(template.render(context, request))

    # return HttpResponse(f"<h1>{post.title}</h1>"
    #                     f"<p>{post.content}</p>")


def detail(request, *args, **kwargs):
    post_id = kwargs.get("post_id")
    post = Post.objects.get(pk=post_id)
    return HttpResponse(f"<h1>{post.title}</h1>"
                        f"<p>{post.content}</p>")


def comment(request, *args, **kwargs):
    comments = Comment.objects.get(pk=1)
    return HttpResponse(f"<p>{comments.text}</p>")