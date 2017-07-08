# -*- coding: utf-8 -*-

from rest_framework import serializers

from todolist.models import TodoList, Label


class TodoListSerializer(serializers.HyperlinkedModelSerializer):

    item_count = serializers.SerializerMethodField()
    label_count = serializers.SerializerMethodField()

    class Meta():
        model = TodoList
        fields = ('id',
                  'title',
                  'created_at',
                  'item_count',
                  'label_count',
                  'labels',
                  'url')

    def get_item_count(self, obj):
        return obj.get_items_count()

    def get_label_count(self, obj):
        return obj.get_label_count()


class LabelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Label
        fields = ('id',
                  'name',
                  'display_name',
                  'url')
        read_only_fields = ('display_name',)
