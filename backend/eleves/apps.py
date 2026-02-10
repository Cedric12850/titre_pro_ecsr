from django.apps import AppConfig

class ElevesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eleves'

    def ready(self):
        import eleves.signals  # <- charge les signaux au démarrage