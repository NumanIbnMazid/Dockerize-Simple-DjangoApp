
from django.contrib import admin
from django.urls import path
from greet.views import hello, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('hello/', hello, name="hello"),
]
