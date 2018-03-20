# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse


def indexcore(request):

    name = request.GET.get('name')
    return HttpResponse('HI {}'.format(name))

# Create your views here.
