"""
URL configuration for ejercicioProductos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from productosApp.views import *
from certamenApp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index),
    path("App1/",App1),
    path("juguetes/",juguetes),
    path("electronica/",electronica),
    path("App2/",App2),
    path("ropa/",ropa),
    path("chile/",chile),
    path("argentina/",argentina),
    path("brasil/",brasil),
    
]
