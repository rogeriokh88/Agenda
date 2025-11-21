from django.db import models
from django.utils import timezone #PARA DATA ATUAL 
from django.contrib.auth.models import User #PARA FAXZER A AUTENTICAÇAO DO USUARIO
# Create your models here.

# id (primary key --automático)
# first_name(string),last_name,phone(string),
# email(email),created_date (data),deccription(text)

# Depois
# category(foreign key),show(boolean)
# picture(imagem),

# Depois
# owner (foreign key)

class Category(models.Model):
    class Meta:
        verbose_name = 'Category' 
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=50)#NOME DA CATEGORIA
    def __str__(self) -> str:
        return self.name

class Contact(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=250,blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    decription = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d') 
    category = models.ForeignKey(#aonde fica a chave estrageira da class Category
        Category, 
        on_delete=models.SET_NULL,#para ficar nulo todos os contatos da categoria que for excluido.
        blank=True, null=True
        )

    
    owner = models.ForeignKey( #para authenticate do usuario.
        User,
        on_delete=models.SET_NULL,#para ficar nulo todo os contato feito pelo usuario excluiido
        blank=True, null=True
        )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
