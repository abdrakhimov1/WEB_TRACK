# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse
from .models import Categories


def categories_show(request):
    context = {
        'categories':Categories.objects.all()
    }

    return render(request, 'categories_show.html', context)

def category_detail(request, pk=None):
    context = {
        'category':Categories.objects.get(id=pk)
    }
    return render(request, 'categories.html', context)
