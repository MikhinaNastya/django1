from django.urls import path

# from blog.views import index, comment

from blog import views

urlpatterns = [
    path('', views.index, name='posts'),
    path('<int:post_id>/', views.detail, name='post-detail'),
    path('comments/', views.comment, name="comments"),
]