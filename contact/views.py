from django.shortcuts import render

# Create your views here.
def index(request): #view da pagina principal do app contact
    print('index')
    return render( #renderiza a pagina html que esta em templates do app contact
        request,
        'contact/index.html',#caminho do arquivo html
    )