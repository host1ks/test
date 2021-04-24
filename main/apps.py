from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        # noinspection PyUnresolvedReferences
        from . import signals