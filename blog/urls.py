from django.urls import path

# from blog.views import index, comment

from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('<int:post_id>/', views.PostDetailView.as_view(), name='post-detail'),
    path('comments/', views.comment, name="comments"),
]


