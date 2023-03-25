from django import forms
from .models import ZisuiPost

class PostForm(forms.ModelForm):

    class Meta:
        model = ZisuiPost
        fields = ('title','image','tag' ,'cost','freetext','created')
        widgets = {
            'created': forms.SelectDateWidget
        }


class EasyPostForm(forms.ModelForm):
    
    class Meta:
        model = ZisuiPost
        fields = ('title','created')
        widgets = {
            'created': forms.SelectDateWidget
        }

        