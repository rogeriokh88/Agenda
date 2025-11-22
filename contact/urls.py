#type:ignore
from django.urls import path #IMPORTA A FUNÇAO PATH PARA CRIAR AS URLS DO APP CONTACT
from contact import views #IMPORTA AS VIEWS DO APP CONTACT

app_name = 'contact'#name space do arquivo urls do app contact

urlpatterns =[
    path('',views.index, name= 'index'),#url principal do app contact
    path('search/',views.search,name='search'),

    # contact(CRUD)
    path('contact/<int:contact_id>/',views.contact, name= 'contact'),
    path('contact/create/',views.create, name= 'create'),
    # path('contact/<int:contact_id>/update/',views.contact, name= 'contact'),
    # path('contact/<int:contact_id>/delete/',views.contact, name= 'contact'),
    
]