from django.db import models
from django.urls import reverse
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag-detail', args=[str(self.id)])

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

class Comment(models.Model):
    text = models.TextField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.text