# -*- coding: utf-8 -*-
import logging

from django.db import models

from django.utils.translation import ugettext as _


logger = logging.getLogger(__name__)


class Label(models.Model):

    name = models.CharField(_("Name"), max_length=20, null=False, blank=False, unique=True)

    foreground_color = models.CharField(_("Foreground Color"), max_length=20,
                                        default='000000', null=False, blank=True)
    background_color = models.CharField(_("Background Color"), max_length=20,
                                        default='ffffff', null=False, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Label"
        verbose_name_plural = "Labels"
        ordering = ['id']


class TodoList(models.Model):

    created_at = models.DateTimeField(_("Created at"), null=False, blank=False, auto_now_add=True)
    title = models.CharField(_("Title"), max_length=50, null=False, blank=False)

    labels = models.ManyToManyField(Label)

    class Meta:
        verbose_name = "TODO-LIST"
        verbose_name_plural = "TODO-LISTs"
        ordering = ['-created_at']

    def get_label_count(self):
        return self.labels.all().count()

    def get_items_count(self):
        return self.items.all().count()


class TodoListItem(models.Model):

    desc = models.CharField(_("Description"), max_length=50, null=False, blank=False)
    done = models.BooleanField(_("Done"), default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name="items")

    class Meta:
        verbose_name = "TODO-LIST Item"
        verbose_name_plural = "TODO-LIST Items"
