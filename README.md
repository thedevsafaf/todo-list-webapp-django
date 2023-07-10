# todo-list-webapp-django
A To Do List web app developed using Django

First clone the repository from Github and switch to the new directory:

$ git clone git@github.com/USERNAME/<project_name>.git

$ cd <project_name>

Setup the project structure:
```
-sample (project folder)
        -src
              -sample (project name)
                      -sample (main app name)
                              -settings.py
                              -urls.py
                              -wsgi.py
                       -app1
                       -app2
                       -appn
                       -requirements.txt
                       -manage.py      
        -venv  
```
Activate the virtualenv for your project.

PROJECT CONFIGURATION if first time
========================================
install virtualenv first
```
pip install --user virtualenv 
```
create virtual environment named venv
```
python -m virtualenv venv
```
activate the venv using activate script
```
venv\Scripts\activate
```
install django in the same venv
```
pip install django
```
to see the installed packages
```
pip freeze
```
install the driver for interacting with PostgreSQL from the Python scripting language
```
pip install psycopg2
```
install postgres for the first time or use sqlite by default
```
depends on the OS

 setup postgres sql
 setup server, username, password, port no. etc
 create database
```
Install project dependencies:
```
$ pip install -r requirements/local.txt
```
Then simply apply the migrations:
```
$ python manage.py migrate
```
You can now run the development server:
```
$ python manage.py runserver
```

![main page](https://github.com/thedevsafaf/todo-list-webapp-django/assets/85129653/860c7a98-ea2f-4017-968d-1623fed204f6)

![todo main page](https://github.com/thedevsafaf/todo-list-webapp-django/assets/85129653/f9fb6d94-3da4-44c0-9b2e-3aecb0000383)

![about page](https://github.com/thedevsafaf/todo-list-webapp-django/assets/85129653/05f323f4-bff8-4f1f-abeb-e3ad979e0921)

![contact page](https://github.com/thedevsafaf/todo-list-webapp-django/assets/85129653/ca0ddca0-0d51-495c-86f0-6fde4de18f36)

