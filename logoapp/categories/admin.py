# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Categories
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):

    pass
