from django.apps import BancoAppConfig


class BancoappConfig(BancoAppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BancoApp'
