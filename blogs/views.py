from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import category,Blog
from django.shortcuts import get_object_or_404
from django.db.models import Q


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
def blogs(request,slug):
     single_blog= get_object_or_404(Blog,slug=slug,status=1)
     context={
          'single_blog':single_blog,
     }
     return render(request,'blogs.html',context)
def search(request):
     keyword=request.GET.get('keyword')
     blogs=Blog.objects.filter(Q(title__icontains=keyword)| Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword))
     context={
          'blogs':blogs,
          'keyword': keyword,
     }
     return render(request,'search.html',context)
     
     


