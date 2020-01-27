# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from community.forms import *

# Create your views here.
def write(request) :
    if request.method == 'post' :
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
            form = Form()

    return render(request, 'write.html', {'form':form})

def list(request):
    boardList = Board.objects.all()
    return render(request, 'list.html', {'boardList':boardList})

def view(request, num="1"):
    board = Board.objects.get(id=num)
    return render(request, 'list.html', {'board':board})

