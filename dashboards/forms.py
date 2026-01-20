from django import forms
from blogs.models import category,Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CategoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = "__all__"
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields =  (
            'title',
            'Category',
            'author',
            'blog_body',
            'status',
            'is_featured',
            'short_description',
            "featured_image",
        )

class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )