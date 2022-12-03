# Bootstrap as first developer / without clone

- $ python -m venv env
- $ source env/bin/activate
- $ pip install -r requirements.txt(While having django in the requirements.txt)
- django-admin startproject myproj
- Move all content from myproj folder outside on root directory
- python manage.py startapp polls
- python manage.py migrate
- python manage.py runserver 0.0.0.0:8000
- debug in pycharm docs/001-pycharm-debug

## setup database


# Install as second developer / after git clone

- \# With python3.9+
- $ python -m venv env
- $ source env/bin/activate
- $ pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver 0.0.0.0:8000
- debug in pycharm docs/001-pycharm-debug

# Debug and run commands in routine

- \# Get into virtual environment
- $ source env/bin/activate
- (On Windows) $ env\Scripts\activate
- python manage.py migrate
- python manage.py runserver 0.0.0.0:8000
- or ./cmd/run (has the same runserver command)
- debug in pycharm docs/001-pycharm-debug

# Create super user like

$ python manage.py createsuperuser

asif : asdf 

# Optimizations

- Watchman(Mac/Linux) ignore large directories for faster reload https://facebook.github.io/watchman/docs/config#ignore_dirs
  - local - the option value is read from the .watchmanconfig file in the associated root.
    global - the option value is read from the /etc/watchman.json file
    fallback - the option value is read from the .watchmanconfig file. If the option was not present in the .watchmanconfig file, then read it from the /etc/watchman.json file.

# Links

## Django installation guide

https://docs.djangoproject.com/en/4.1/intro/install/

## Database setup

https://docs.djangoproject.com/en/4.1/topics/install/#database-installation

## Postgres Setup

https://docs.djangoproject.com/en/4.1/ref/databases/#postgresql-notes


# Git
Repo: https://github.com/asifashraf/poc_django 

### checkpoint
https://docs.djangoproject.com/en/4.1/intro/tutorial02/