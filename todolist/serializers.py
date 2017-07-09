# -*- coding: utf-8 -*-
from rest_framework.reverse import reverse_lazy
from rest_framework import serializers

from todolist.models import TodoList, Label, TodoListItem


class LabelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Label
        fields = ('id',
                  'name',
                  'url')
        read_only_fields = ('id',)


class TodoListItemSerializer(serializers.ModelSerializer):

    class Meta():
        model = TodoListItem
        fields = ('id',
                  'desc',
                  'done',
                  'todo_list',
                  )
        read_only_fields = ('todo_list',)


class TodoListSerializer(serializers.HyperlinkedModelSerializer):

    item_count = serializers.SerializerMethodField()
    label_count = serializers.SerializerMethodField()

    labels = LabelSerializer(many=True)

    items_url = serializers.SerializerMethodField()

    class Meta():
        model = TodoList
        fields = ('id',
                  'title',
                  'created_at',
                  'item_count',
                  'label_count',
                  'labels',
                  'url',
                  'items_url')

    def get_item_count(self, obj):
        return obj.get_items_count()

    def get_label_count(self, obj):
        return obj.get_label_count()

    def get_items_url(self, obj):
        return reverse_lazy('todolist-items-list', args=[obj.pk], request=self.context.get('request'))
