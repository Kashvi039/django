from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogForm,AddUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    categories_count=category.objects.count()
    posts_count=Blog.objects.count()
    context={
        "categories_count" :  categories_count,
        "posts_count": posts_count,


    }
    return render(request,'dashboard/dashboard.html',context)
def categories(request):
    return render(request,'dashboard/categories.html')
def addCategory(request):
    if(request.method == 'POST'):
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')

    form=CategoryForm()
    context={
        'form':form,
    }
    return render(request,'dashboard/addCategory.html',context)
def editCategory(request, pk):
    category_obj = get_object_or_404(category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category_obj)
        if form.is_valid():
            form.save()   # 🔁 update existing
            return redirect('categories')
    else:
        form = CategoryForm(instance=category_obj)  # pre-filled form

    return render(request, 'dashboard/editCategory.html', {'form': form})
def deleteCategory(request,pk):
     category_obj = get_object_or_404(category, pk=pk)
     category_obj.delete()
     return redirect('categories')
def posts(request):
    posts=Blog.objects.all()
    context={
        'posts':posts,
    }
    return render(request, 'dashboard/posts.html',context)

def addPost(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            title=form.cleaned_data[title]
            post.slug= slugify(title)
            
            return redirect('posts')     
    else:
        form = BlogForm()

    context = {
        'form': form,
    }
    return render(request, 'dashboard/addPost.html', context)
def editpost(request,pk):
    category_obj = get_object_or_404(Blog, pk=pk)
                                                 
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=category_obj)
        if form.is_valid():
            form.save()   # 🔁 update existing
            return redirect('posts')
    else:
        form = BlogForm(instance=category_obj)  # pre-filled form
    context={
        'form': form,
    }

    
    return render(request,'dashboard/editpost.html',context)
def delpost(request,pk):
     category_obj = get_object_or_404(Blog, pk=pk)
     category_obj.delete()
     return redirect('posts')
def users(request):
    users=User.objects.all()     
    context={
        'users': users,
    }
    return render(request,'dashboard/users.html',context)
def add_users(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')   # users = users list page url name
    else:
        form = AddUserForm()

    context = {
        'form': form,
    }

    return render(request, 'dashboard/add_users.html', context)