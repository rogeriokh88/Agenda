from django.urls import path #IMPORTA A FUNÇAO PATH PARA CRIAR AS URLS DO APP CONTACT
from contact import views #IMPORTA AS VIEWS DO APP CONTACT

app_name = 'contact'#name space do arquivo urls do app contact

urlpatterns =[
    path('',views.index, name= 'index')#url principal do app contact
]