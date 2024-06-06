from django.db import models

from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.pk})"


class Post(models.Model):

    title = models.CharField(max_length=100)  # VARCHAR(100) NOT NULL
    content = models.TextField()  # TEXT NOT NULL UNIQUE

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # User.posts.all()

    categories = models.ManyToManyField(Category)  # Category.posts.all()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "posts"
        ordering = ("-created_at",)
        unique_together = ("title", "content", "author")
        indexes = [models.Index(fields=("title", "content", "created_at"))]
        default_related_name = "posts"

    @property
    def demo_text(self):
        return f"{self.content[:10]}..."

    def __str__(self):
        return f"{self.title} ({self.pk})"  # pk = primary key


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")  # related_name: comment_set
    text = models.CharField(max_length=200)  # VARCHAR NOT NULL

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.text} ({self.pk})"

