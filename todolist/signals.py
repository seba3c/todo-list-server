# -*- coding: utf-8 -*-
import logging

from django.db.models.signals import pre_save
from django.dispatch import receiver

from todolist.models import Label

logger = logging.getLogger(__name__)


@receiver(pre_save, sender=Label)
def label_pre_save_signal(sender, instance, **kwargs):
    # do something before save
    pass
