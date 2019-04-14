from django.apps import AppConfig


class AioConfig(AppConfig):
    name = 'aio'

    # def ready(self):
    #     import aio.signals