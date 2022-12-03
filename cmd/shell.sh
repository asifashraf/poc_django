cd ..
python manage.py shell

#We’re using this instead of simply typing “python”,
# because manage.py sets the DJANGO_SETTINGS_MODULE environment variable,
# which gives Django the Python import path to your mysite/settings.py file.