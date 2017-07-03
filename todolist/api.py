# -*- coding: utf-8 -*-
import logging

from rest_framework import viewsets

from todolist.models import TodoList
from todolist.serializers import TodoListSerializer

logger = logging.getLogger(__name__)


class TodoListViewSet(viewsets.ModelViewSet):

    model = TodoList
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()
