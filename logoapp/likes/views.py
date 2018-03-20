# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def indexlikes(request):
    return HttpResponse('HI, Im likes')

# Create your views here.
