from django.db import models
from django.utils import timezone
# Create your models here.

#id (primary key --automático)
#first_name(string),last_name,phone(string),
#email(email),created_date (data),deccription(text)

#depois
#category(foreign key),show(boolean)
#picture(imagem),owner (foreign key)

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length= 250)
    created_date = models.DateTimeField(default=timezone.now)
    decription = models.TextField(blank=True)

