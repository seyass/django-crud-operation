from django.apps import AppConfig
from django.db.models.signals import post_save


def example_reciver(sender,**kwargs):
    print('instance is saved')



class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def reaedy(self)-> None:
        post_save
