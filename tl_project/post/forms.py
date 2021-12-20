from django import forms
from django.contrib.auth.models import User
from django import forms
from .models import Post, UploadModel
from members.models import Member

class UploadFileForm(forms.Form):
    file = forms.FileField()