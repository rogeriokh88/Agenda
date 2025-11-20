Iniciar o projeto Django

'''
python -m venv venv
.venv/scripts/activate
pip install django 
django-admin startproject project .
python manage.py startapp contact
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
