# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import post

# Register your models here.

@admin.register(post)
class PostAdmin(admin.ModelAdmin):

    pass