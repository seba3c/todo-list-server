# -*- coding: utf-8 -*-

from rest_framework import serializers

from todolist.models import TodoList


class TodoListSerializer(serializers.Serializer):

    class Meta:
        model = TodoList
        fields = ('id',
                  'title',
                  'created_at')
