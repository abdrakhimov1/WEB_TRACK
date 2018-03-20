# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin as OldUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(OldUserAdmin):

    pass
