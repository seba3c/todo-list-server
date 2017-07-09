# -*- coding: utf-8 -*-
import logging

from rest_framework import viewsets

from todolist.models import TodoList, Label, TodoListItem
from todolist.serializers import (TodoListSerializer,
                                  LabelSerializer, TodoListItemSerializer)
from django.http.response import Http404

logger = logging.getLogger(__name__)


class TodoListViewSet(viewsets.ModelViewSet):

    model = TodoList
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()


class LabelViewSet(viewsets.ModelViewSet):

    model = Label
    serializer_class = LabelSerializer
    queryset = Label.objects.all()


class TodoListItemViewSet(viewsets.ModelViewSet):

    model = TodoListItem
    serializer_class = TodoListItemSerializer

    def get_todolist(self):
        todolist_pk = self.kwargs.get('todolist_pk', -1)
        try:
            return TodoList.objects.get(pk=todolist_pk)
        except TodoList.DoesNotExist:
            raise Http404

    def get_queryset(self):
        todolist = self.get_todolist()
        return TodoListItem.objects.filter(todo_list=todolist)

    def perform_create(self, serializer):
        todolist = self.get_todolist()
        serializer.save(todo_list=todolist)
