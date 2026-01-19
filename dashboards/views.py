from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm

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

