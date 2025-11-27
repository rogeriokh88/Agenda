from django.shortcuts import redirect, render 
from contact.forms import ContactForm

def create(request): #view da pagina principal do app contact
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('contact:create',)

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