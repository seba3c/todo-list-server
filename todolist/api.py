# -*- coding: utf-8 -*-
import logging

from rest_framework import viewsets

from todolist.models import TodoList, Label
from todolist.serializers import (TodoListSerializer,
                                  LabelSerializer)

logger = logging.getLogger(__name__)


class TodoListViewSet(viewsets.ModelViewSet):

    model = TodoList
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()


class LabelViewSet(viewsets.ModelViewSet):

    model = Label
    serializer_class = LabelSerializer
    queryset = Label.objects.all()
