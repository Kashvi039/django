from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import category,Blog, Comment
from django.shortcuts import get_object_or_404
from django.db.models import Q
from blog.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
app_name = 'blogs'



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
     comments = Comment.objects.filter(blog=single_blog)
     context={
          'single_blog':single_blog,
          'comments':comments,
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
def register(request):
     if request.method == 'POST':
          form=RegistrationForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('register')


     else:
          form=RegistrationForm()
     context={
          'form':form,
     }
     return render(request,'register.html',context)
def login(request):
     if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
                                                   
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
            return redirect('dashboard')
     form= AuthenticationForm()
     context={
          'form': form        
     }
     return render(request,'login.html',context)
def logout(request):                                                                                          
     auth.logout(request)   
     return redirect('home')                                                     
    
     
     


