Iniciar o projeto Django

'''
python -m venv venv
.venv/scripts/activate
pip install django 
django-admin startproject project .
python manage.py startapp contact
pip install pillow para amazenar o aquivo imagem na pasta media.
para consula os aquivo install no ambiente vitual 
para atualiza o git com arquivo novo
git add .
git commit -m 'string'
git push
'''
configurar o git
'''
'configure o gitignore'
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultbranch main
git init
git add .
git commit -m 'Mensagem'
git remote add origin https://github.com/roegeriokh88/Agenda.git
git push -u origin main

'''
para vê o commit : git log ou git log --oneline


'''para configura as pasta static tem que ir no arquivo settings.py depois criar o arquivo
STATICFILES_DIRS = (
    BASE_DIR / 'nome da pasta',
)


''' comados ''
Migrando a base de dados Django
'''
python manage.py makemigrations
python manage.py migrate
'''

Criando e modificando a senha de um super usuario Django

'''
python manage.py createsuperuser
python manage.py changepassword USERNAME
quando esquece a senha usar comando "python manage.py changepassword nome do usuario"
'''
Trabalho com Django
'''python
#importe o módulo
from contact.models import Contact
#criar um contato(Lazy)
#retona o contato
contact = Contact(**fields)
contact.save()
#cria um contact (não Lazy)
#returna o contato
contact = Contact.objects.create(**fields)
#Seleciona um contato com id 10
#retorna o contato
contact = Contact.objects.get(pk=10)
#Edita um contato
#retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor2'
contact.save()
#apaga um contato
#Depende da base de dados,geralmente retorna o número
#de valores manipulado na base de dados 
contact.delete()
#seleciona todos os contatos ordenado por id DESC
#retorna QuerySet[]
contacts = Contact.objects.all().order_by('-iod')
#seleciona contatos usando filtros
#Retorna QuerySet[]
contact = Contact.objects.filter(**filters).order_by('-id')
'''