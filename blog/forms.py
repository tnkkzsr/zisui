from django import forms
from .models import ZisuiPost

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label#全てのフォームの部品にplaceholderを定義して、入力フォームにフォーム名が表示されるように指定


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
            'created': forms.SelectDateWidget }