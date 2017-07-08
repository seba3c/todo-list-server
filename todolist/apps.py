from django.apps import AppConfig


class TodolistConfig(AppConfig):
    name = 'todolist'
    verbose_name = u'TO-DO List App'

    def ready(self):
        import todolist.signals
