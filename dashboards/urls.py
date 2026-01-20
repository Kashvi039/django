from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('categories/',views.categories,name='categories'),
    path('categories/add/',views.addCategory,name='addCategory'),
    path('categories/edit/<int:pk>/',views.editCategory,name='editCategory'),
    path('categories/delete/<int:pk>/',views.deleteCategory,name='deleteCategory'),
    path('posts/',views.posts,name='posts'),
    path('posts/add/',views.addPost,name='addPost'),
   path('posts/edit/<int:pk>/',views.editpost,name='editpost'),
    path('posts/delete/<int:pk>/',views.delpost,name='delpost'),
   path('users/',views.users,name='users'),
   path('users/add/',views.add_users,name='add_users'),
       
      
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
