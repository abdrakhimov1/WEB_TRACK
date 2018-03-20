# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse

def post_show(request, post_ID):
    return HttpResponse('Post # {}'.format(post_ID))

# Create your views here.
