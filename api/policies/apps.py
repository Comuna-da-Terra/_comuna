from django.apps import AppConfig


class PoliciesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'policies'

    def ready(self):
        from . import signals  # Importando o arquivo para registrar o signal