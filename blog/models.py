from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

# Create your models here.
class Article(models.Model):
    title = models.CharField("titre", max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title