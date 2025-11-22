from django.shortcuts import render , get_object_or_404, redirect
#from django.http import Http404
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator

# Create your views here.
def create(request): #view da pagina principal do app contact
    context = {

    }

    return render(
        request,
        'contact/create.html',
        context,
    )