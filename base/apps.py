from django.apps import AppConfig

# this is where settings.py will point to
class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
