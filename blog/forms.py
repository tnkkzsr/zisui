from django import forms
from .models import ZisuiPost

class PostForm(forms.ModelForm):

    class Meta:
        model = ZisuiPost
        fields = ('title','author','image','tag' ,'cost','ingredients','howtocook','freetext')
