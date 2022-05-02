from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Book(models.Model):
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    title = models.CharField(max_length=120, verbose_name='Название')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="media/image/")

    def __str__(self):
        return f"{self.title}-{self.id}"


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
