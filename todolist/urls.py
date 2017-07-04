# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from rest_framework.routers import SimpleRouter

from todolist.api import TodoListViewSet1

API_VERSION = 'v1'

API_PREFIX = "api/%s" % API_VERSION

api_router = SimpleRouter()

api_router.register(r'%s/todolist-1' % API_PREFIX,
                    TodoListViewSet1, base_name='todolist-1')

urlpatterns = [url(r'^', include(api_router.urls)),
               ]
