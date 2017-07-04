# -*- coding: utf-8 -*-
import logging

from rest_framework import viewsets

from todolist.models import TodoList
from todolist.serializers import TodoListSerializer1

logger = logging.getLogger(__name__)


class TodoListViewSet1(viewsets.ModelViewSet):

    model = TodoList
    serializer_class = TodoListSerializer1
    queryset = TodoList.objects.all()
