from django import forms
from .models import ZisuiPost

class PostForm(forms.ModelForm):

    class Meta:
        model = ZisuiPost

        fields = ('image','title','author','ingredients','cost','howtocook','freetext')
