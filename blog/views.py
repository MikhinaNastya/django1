from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader

from blog.models import Post, Comment


def index(request, *args, **kwargs):
    posts = Post.objects.all()

    context = {
        "my_posts": posts,
        "name": "Arman",
    }

    # template = loader.get_template('blog/index.html')
    # return HttpResponse(template.render(context, request))
    return render(
        request=request,
        template_name='blog/index.html',
        context=context
    )


def detail(request, *args, **kwargs):
    post_id = kwargs.get("post_id")
    post = Post.objects.get(pk=post_id)
    return HttpResponse(f"<h1>{post.title}</h1>"
                        f"<p>{post.content}</p>")


def comment(request, *args, **kwargs):
    comments = Comment.objects.get(pk=1)
    return HttpResponse(f"<p>{comments.text}</p>")