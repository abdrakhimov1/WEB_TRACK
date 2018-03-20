# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.conf import settings



# Create your models here.
from categories.models import Categories


class post(models.Model):


    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    categories = models.ManyToManyField(Categories, blank=True, related_name='posts')
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name