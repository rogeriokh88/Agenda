Iniciar o projeto Django

'''
python -m venv venv
.venv/scripts/activate
pip install django 
django-admin startproject project .
python manage.py startapp contact
para consula os aquivo install no ambiente vitual 
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