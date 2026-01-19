from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dasboard/', views.dashboard, name="dashboard"),
    path('categories/',views.categories,name='categories'),
     path('categories/add/',views.addCategory,name='addCategory'),
     path('categories/edit/<int:pk>/',views.editCategory,name='editCategory'),
      path('categories/delete/<int:pk>/',views.deleteCategory,name='deleteCategory'),
    
      
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
