from django import views
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import PostModelForm
from blog.models import Post, Comment


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'my_posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["user"] = "Ulan"
        return context


class PostCreateView(generic.CreateView):
    form_class = PostModelForm
    template_name = "blog/create_post.html"
    success_url = reverse_lazy("posts")


class PostCreateViewOld(views.View):

    def get(self, request, *args, **kwargs):
        context = {
            'my_form': PostModelForm()
        }
        return render(
            request=request,
            template_name='blog/create_post.html',
            context=context
        )

    def post(self, request, *args, **kwargs):
        form = PostModelForm(request.POST)

        if form.is_valid():
            new_post = form.save()

            return redirect("post-detail", new_post.pk)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    pk_url_kwarg = "post_id"


class PostDetailViewOld(views.View):

    def get(self, request, *args, **kwargs):
        post_id = kwargs.get("post_id")
        post = Post.objects.get(pk=post_id)
        context = {
            'post': post
        }

        return render(
            request=request,
            template_name="blog/post_detail.html",
            context=context)


def comment(request, *args, **kwargs):
    comments = Comment.objects.get(pk=1)
    return HttpResponse(f"<p>{comments.text}</p>")