# -*- coding: utf-8 -*-

from rest_framework import serializers

from todolist.models import TodoList, Label


class TodoListSerializer1(serializers.ModelSerializer):

    class Meta:
        model = TodoList
        fields = ('id',
                  'title',
                  'created_at')


class TodoListSerializer2(TodoListSerializer1):

    item_count = serializers.SerializerMethodField()
    label_count = serializers.SerializerMethodField()

    class Meta(TodoListSerializer1.Meta):
        fields = TodoListSerializer1.Meta.fields + ('item_count',
                                                    'label_count')

    def get_item_count(self, obj):
        return obj.get_items_count()

    def get_label_count(self, obj):
        return obj.get_label_count()


class TodoListSerializer3(TodoListSerializer2):

    class Meta(TodoListSerializer2.Meta):
        fields = TodoListSerializer2.Meta.fields + ('labels', )


class LabelSerializer1(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = ('id',
                  'name')


class LabelSerializer2(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='labels-2-detail')

    class Meta:
        model = Label
        fields = ('id',
                  'name',
                  'url')
