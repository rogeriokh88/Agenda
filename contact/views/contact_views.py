from django.shortcuts import render , get_object_or_404, redirect
#from django.http import Http404
from django.db.models import Q
from contact.models import Contact

# Create your views here.
def index(request): #view da pagina principal do app contact
    contacts = Contact.objects \
        .filter(show=True) \
        .order_by('-id')[:10]
        #objects pega todos os contatos do banco de dados 
        #filter pega so os contatos que estao com show= true
        #order_by ordena os contatos pelo id de forma decrecente
    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }

    return render( #renderiza a pagina html que esta em templates do app contact
        request,
        'contact/index.html',#caminho do arquivo html
        context,  
        )


def contact(request, contact_id): #view da pagina principal do app contact
    #single_contact = Contact.objects.filter(pk=contact_id).last() #get pega um coisa unica
    single_contact = get_object_or_404(Contact,pk=contact_id,show=True,)#ataho a funçao get object_or_404 para pegar o contato ou gerar um erro 404
    #contact_id vem da url que esta em contact/urls.py
    #pk= contact_id primary key igual ao contact_id
    #if single_contact is None: para gerar um erro 404 caso o contato nao exista 
     #   raise Http404('Contato não encontrado!')'''
    contact_name = f'{single_contact.first_name}{single_contact.last_name} -'

    context = {
        'contact': single_contact,
        'site_title': contact_name,
        
    }

    return render( #renderiza a pagina html que esta em templates do app contact
        request,
        'contact/contact.html',#caminho do arquivo html
        context,  
        )

def search(request): #view da pagina principal do app contact
    search_value = request.GET.get('q','').strip()
    print(search_value)

    if search_value == '':
        return redirect('contact:index')
    
    contacts = Contact.objects \
        .filter(show=True) \
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
            )\
        .order_by('-id')
        #objects pega todos os contatos do banco de dados 
        #filter pega so os contatos que estao com show= true
        #order_by ordena os contatos pelo id de forma decrecente
    context = {
        'contacts': contacts,
        'site_title': 'search - '
    }

    return render( #renderiza a pagina html que esta em templates do app contact
        request,
        'contact/index.html',#caminho do arquivo html
        context,  
        )
