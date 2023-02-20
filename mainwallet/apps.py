from django.apps import AppConfig


class MainwalletConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainwallet'
    def ready(self):
        print("starting scheduler .....")
        from utils import functions
        functions.start()


#python manage.py runserver --noreload