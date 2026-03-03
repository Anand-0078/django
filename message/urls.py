from django.contrib import admin
from django.urls import path
from .views import home   # correct relative import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
]