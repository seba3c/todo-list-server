# -*- coding: utf-8 -*-
import logging

from django.db import models

from django.utils.translation import ugettext as _


logger = logging.getLogger(__name__)


class TodoList(models.Model):

    created_at = models.DateTimeField(_("Created at"), null=False, blank=False, auto_now_add=True)
    title = models.CharField(_("Title"), max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = "TODO-LIST"
        verbose_name_plural = "TODO-LISTs"
        ordering = ['-created_at']


class TodoListItem(models.Model):

    desc = models.CharField(_("Description"), max_length=50, null=False, blank=False)
    done = models.BooleanField(_("Done"), default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name="items")

    class Meta:
        verbose_name = "TODO-LIST Item"
        verbose_name_plural = "TODO-LIST Items"
