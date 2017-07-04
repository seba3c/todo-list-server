# -*- coding: utf-8 -*-

from rest_framework import serializers

from todolist.models import TodoList


class TodoListSerializer1(serializers.ModelSerializer):

    class Meta:
        model = TodoList
        fields = ('id',
                  'title',
                  'created_at')
