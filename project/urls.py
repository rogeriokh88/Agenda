"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin #IMPORTA O ADMIN DO DJANGO
from django.urls import path, include #IMPORTA A FUNÇAO PATH E INCLUDE PARA CRIAR AS URLS DO PROJETO
from django.conf.urls.static import static #IMPORTA PARA CONFIGURAR AS URL DE ARQUIVOS ESTATICOS DE MIDIA E STATIC FILES
from django.conf import settings #IMPORTA AS CONFIGURAÇAO DO PROJETO SETTINGS.PY PARA USER NAS URLS

urlpatterns = [
    path('',include('contact.urls')), #INCLUI AS URLS DO APP CONTACT NA URL PRINCIPAL DO PROJETO
    path('admin/', admin.site.urls), #URL DO ADMINISTRADOR DO DJANGO
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #CONFIGURA AS URLS DE MIDIA
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) #CONFIGURA AS URLS DE STARTIC FILES 