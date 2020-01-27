# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Board(models.Model) :
        name = models.CharField(max_length=50)
        title = models.CharField(max_length=50)
        contents = models.TextField()
        url = models.URLField()
        email = models.EmailField()
        cdate = models.DateTimeField(auto_now_add = True)