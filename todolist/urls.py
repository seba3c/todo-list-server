# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from rest_framework.routers import SimpleRouter
from todolist.api import TodoListViewSet

API_VERSION = 'v1'

API_PREFIX = "api/%s" % API_VERSION

api_router = SimpleRouter()

api_router.register(r'%s/todolist' % API_PREFIX,
                    TodoListViewSet, base_name='todolist')

urlpatterns = [url(r'^', include(api_router.urls)),
               ]
