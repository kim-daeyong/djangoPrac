from django.forms import ModelForm
from community.models import *

class Form(ModelForm) :
    class Meta :
        model = Board
        fields = ['name', 'title', 'contents', 'url', 'email']