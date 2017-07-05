# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from rest_framework.routers import SimpleRouter

from todolist.api import (TodoListViewSet1,
                          TodoListViewSet2,
                          TodoListViewSet3,
                          LabelViewSet1,
                          LabelViewSet2)

API_VERSION = 'v1'

API_PREFIX = "api/%s" % API_VERSION

api_router = SimpleRouter()

api_router.register(r'%s/todolist-1' % API_PREFIX,
                    TodoListViewSet1, base_name='todolist-1')

api_router.register(r'%s/todolist-2' % API_PREFIX,
                    TodoListViewSet2, base_name='todolist-2')

api_router.register(r'%s/todolist-3' % API_PREFIX,
                    TodoListViewSet3, base_name='todolist-3')

api_router.register(r'%s/labels-1' % API_PREFIX,
                    LabelViewSet1, base_name='labels-1')

api_router.register(r'%s/labels-2' % API_PREFIX,
                    LabelViewSet2, base_name='labels-2')

urlpatterns = [url(r'^', include(api_router.urls)),
               ]
