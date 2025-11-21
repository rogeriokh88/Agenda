from django.contrib import admin
from contact import models
# Register your models here.

@admin.register(models.Contact) #decorator para registrar a class contact no admin
class ContactAdmin(admin.ModelAdmin):#configuraçoes do admin para a class contact
    list_display = ('id','first_name', 'last_name','phone','email','created_date')#coluna a ser exibida na pagina do admin
    ordering = ('-id',)#ordenaçao
    #list_filter = 'created_date',
    search_fields = 'id','first_name','last_name',#campo de pesquis 
    list_per_page = 10 #NUMERO DE ITENS POR PAGINA
    list_max_show_all = 200 #NUMERO MAXIMO DE ITENS QUE PODE SER EXIBIDO NA PAGINA DO ADMIN
    list_editable = 'first_name','last_name',#CAMPO EDITAVEL NA PAGINA DO ADMIN
    list_display_links = 'id','phone',#CAMPO QUE SERA LINK PARA EDITAR O ITENS NA PAGINA DO ADMIN

@admin.register(models.Category)#DECORATPR PARA REGISTRAR A CLASS CATEGOLRY NO ADMIN 
class CategoryAdmin(admin.ModelAdmin):#CONFIGURAÇOES DO ADMIN PARA A CLASS CATEGORY
    list_display = ('name',)#COLUNA A SER EXIBIDA NA PAGINA DO ADMIN
    ordering = ('-id',)#ORDENADO
   