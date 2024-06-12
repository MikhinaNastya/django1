from django import views
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader

from blog.forms import PostModelForm
from blog.models import Post, Comment


def index(request, *args, **kwargs):
    posts = Post.objects.all()

    context = {
        "my_posts": posts,
        "name": "Arman",
    }

    return render(
        request=request,
        template_name='blog/index.html',
        context=context
    )


def create_post(request, *args, **kwargs):

    print(f"request method: {request.method}")

    if request.method == "GET":
        context = {
            'my_form': PostModelForm()
        }
        return render(
            request=request,
            template_name='blog/create_post.html',
            context=context
        )
    elif request.method == "POST":
        form = PostModelForm(request.POST)

        if form.is_valid():
            # title = form.cleaned_data["title"]

            # new_post = form.save(commit=False)
            # new_post.author_id = 1
            # new_post.save()

            new_post = form.save()

            return redirect("post-detail", new_post.pk)

    return HttpResponse(f"<h1>Not Allowed!</h1>")


def create_post_old(request, *args, **kwargs):

    if request.method == "GET":
        return render(
            request=request,
            template_name='blog/create_post.html',
        )
    elif request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        author_id = 1

        new_post = Post(
            title=title,
            content=content,
            author_id=author_id
        )

        new_post.save()
        return redirect("post-detail", new_post.pk)

        # return HttpResponse(f"<h1>Post Created!</h1>"
        #                     f"<h2>{new_post.pk}. {new_post.title}</h2>"
        #                     f"<p>{new_post.content}</p>")

    return HttpResponse(f"<h1>Not Allowed!</h1>")


def detail(request, *args, **kwargs):
    post_id = kwargs.get("post_id")
    post = Post.objects.get(pk=post_id)
    return HttpResponse(f"<h1>{post.pk}.{post.title}</h1>"
                        f"<p>{post.content}</p>")


def comment(request, *args, **kwargs):
    comments = Comment.objects.get(pk=1)
    return HttpResponse(f"<p>{comments.text}</p>")
