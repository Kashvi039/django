from django import forms
from blogs.models import category,Blog


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

