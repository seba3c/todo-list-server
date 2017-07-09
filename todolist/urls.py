# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include

from rest_framework.routers import SimpleRouter

from todolist.api_examples import (TodoListViewSet1,
                                   TodoListViewSet2,
                                   TodoListViewSet3,
                                   LabelViewSet1,
                                   LabelViewSet2)

from todolist.api import (TodoListViewSet,
                          LabelViewSet, TodoListItemViewSet)

API_VERSION = 'v1'

API_PREFIX = "api/%s" % API_VERSION

api_router = SimpleRouter()

if settings.ENABLE_EXAMPLES:
    api_router.register(r'%s/todolist-ex1' % API_PREFIX,
                        TodoListViewSet1, base_name='todolist-ex1')

    api_router.register(r'%s/todolist-ex2' % API_PREFIX,
                        TodoListViewSet2, base_name='todolist-ex2')

    api_router.register(r'%s/todolist-ex3' % API_PREFIX,
                        TodoListViewSet3, base_name='todolist-ex3')

    api_router.register(r'%s/labels-ex1' % API_PREFIX,
                        LabelViewSet1, base_name='labels-ex1')

    api_router.register(r'%s/labels-ex2' % API_PREFIX,
                        LabelViewSet2, base_name='labels-ex2')

api_router.register(r'%s/todolists' % API_PREFIX,
                    TodoListViewSet, base_name='todolist')

api_router.register(r'%s/labels' % API_PREFIX,
                    LabelViewSet, base_name='label')

api_router.register(r'%s/todolists/(?P<todolist_pk>[0-9]+)/items' % API_PREFIX,
                    TodoListItemViewSet,
                    base_name='todolist-items')

urlpatterns = [url(r'^', include(api_router.urls)),
               ]
