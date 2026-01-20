from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class category(models.Model):
    category_name= models.CharField(max_length=50,unique=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.category_name
STATUS_CHOICES = (
        (0, "Draft"),
        (1, "Published"),
    )

class Blog(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=150,unique=True)
    Category=models.ForeignKey(category,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image = models.ImageField(
        upload_to='uploads/%Y/%m/%d',
        blank=True,
        null=True
    )

    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)

    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=0
    )

    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body