from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
]