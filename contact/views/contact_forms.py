from django.shortcuts import render 
from contact.forms import ContactForm



def create(request): #view da pagina principal do app contact
    if request.method == 'POST':
         context = {
        'form': ContactForm(request.POST),
        }
         return render(
                request,
                'contact/create.html',
                context,
                )
         
    context = {
        'form': ContactForm(),
    }
    return render(
                request,
                'contact/create.html',
                context,
                )