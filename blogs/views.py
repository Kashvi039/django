from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import category,Blog

# Create your views here.
def home(request):
    categories= category.objects.all()
    featured_posts=Blog.objects.filter(is_featured=True,status='1')
    posts=Blog.objects.filter(is_featured=False,status='1')
    context = {
        'categories' : categories,
        "featured_posts": featured_posts,
        'posts':posts,
    }                            
          
    return render(request,'home.html',context)
def postsbycategory(request,category_id):
     posts=Blog.objects.filter(is_featured=True,Category_id=category_id)
     context={
          'posts':posts,
     }
     return render(request, 'postsbycategory.html', context)


