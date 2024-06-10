from django.urls import path

# from blog.views import index, comment

from blog import views

urlpatterns = [
    path('', views.index),
    path('<int:post_id>/', views.detail),
    path('comments/', views.comment),
]