# -*- coding: utf-8 -*-
import logging

from rest_framework import viewsets

from todolist.models import TodoList, Label
from todolist.serializers import (TodoListSerializer1,
                                  TodoListSerializer2,
                                  TodoListSerializer3,
                                  LabelSerializer1,
                                  LabelSerializer2)

logger = logging.getLogger(__name__)


class TodoListViewSet1(viewsets.ModelViewSet):

    model = TodoList
    serializer_class = TodoListSerializer1
    queryset = TodoList.objects.all()


class TodoListViewSet2(viewsets.ModelViewSet):

    model = TodoList
    serializer_class = TodoListSerializer2
    queryset = TodoList.objects.all()

    def get_view_name(self):
        return "TO-DO List endpoint 2"


class TodoListViewSet3(TodoListViewSet1):

    serializer_class = TodoListSerializer3


class LabelViewSet1(viewsets.ModelViewSet):

    model = Label
    serializer_class = LabelSerializer1

    def get_queryset(self):
        return Label.objects.all()


class LabelViewSet2(viewsets.ReadOnlyModelViewSet):

    model = Label
    serializer_class = LabelSerializer2
    queryset = Label.objects.all()
