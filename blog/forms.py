from django import forms
from .models import ZisuiPost

class PostForm(forms.ModelForm):

    class Meta:
        model = ZisuiPost
        fields = ('title','image','tag' ,'cost','freetext',)


class EasyPostForm(forms.ModelForm):
    
    class Meta:
        model = ZisuiPost
        fields = ('title',)

        