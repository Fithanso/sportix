# sportix
Sports exercise accounting system in a form of RESTful API

#### API's documentation is available on http://127.0.0.1:8000/swagger/

#### Django Admin is on http://127.0.0.1:8000/admin/

Credentials: 
```
Username: fithanso
Password: nadezhnyi
```


Tests can be run with:
```
python manage.py test apps.accounts.test_endpoints
python manage.py test apps.sports.test_endpoints
```


## Deployment instructions:

1. First, install following packages using ```apt install```:
```
nginx, supervisor, python3.10
```
Install _**Poetry**_ using the <a href="https://python-poetry.org/docs/#installing-with-the-official-installer">official guide</a>.
Make sure to add Poetry to PATH and check that your ```/home/[username]/.local/bin/``` contains Poetry executable.  
2. Clone the repo. It is recommended to clone it into /home/projects/ directory, as all config files assume this is where the project resides.  
3. Enter project's root directory and run ```poetry install``` to install all dependencies.  
4. Edit ```sportix/conf/sportix.uwsgi.conf``` file and specify your username here: ```command=/home/[user]/.local/bin/poetry run uwsgi conf/sportix_uwsgi.ini```  
5. Create ```.env``` file in the project's root. Specify following variables:  
```
DJANGO_SECRET_KEY=[your secret key]
DEBUG=[True or False]
```  
6. Run following commands:
```
python manage.py migrate
python manage.py collectstatic
python manage.py loaddata accounts.json sports.json
```  
7. Create symlink to your NGINX's 'sites-enabled' directory for ```sportix/conf/sportix_nginx.conf``` file.  
8. Create symlink for ```sportix/conf/sportix.uwsgi.conf``` into ```/etc/supervisor/conf.d```.  
9. Run ```sudo systemctl start supervisor``` (or ```sudo systemctl restart supervisor```). Check that process "sportix_uwsgi" is running by ```sudo supervisorctl status```.  
10. Start NGINX. Website should work on http://127.0.0.1:8000.  

