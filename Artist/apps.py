from django.apps import AppConfig


class ArtistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Artist'
    # only the following bit is added
    def ready(self):
        import Artist.signals
