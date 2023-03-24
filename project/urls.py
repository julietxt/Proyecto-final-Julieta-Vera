"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from VentaLibre.views import (index, ArticuloList, ArticuloMineList,ArticuloUpdate, ArticuloDelete, ArticuloCreate, Login, Logout, SignUp)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('articulo/list', ArticuloList.as_view(), name="articulo-list"),
    path('articulo/list', ArticuloMineList.as_view(), name="articulo-mine"),
    path('articulo/<pk>/update', ArticuloUpdate.as_view(), name="articulo-update"),
    path('articulo/<pk>/delete', ArticuloDelete.as_view(), name="articulo-delete"),
    path('articulo/create', ArticuloCreate.as_view(), name="articulo-create"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('signup/', SignUp.as_view(), name="signup"),
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)