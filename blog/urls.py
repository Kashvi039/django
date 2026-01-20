from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # public blog app
    path('', include('blogs.urls')),

    # dashboard app
    path('dashboard/', include('dashboards.urls')),
]
