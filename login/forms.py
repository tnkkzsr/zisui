from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import User



class LoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label#全てのフォームの部品にplaceholderを定義して、入力フォームにフォーム名が表示されるように指定

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('email','username', 'years','living_alone')
    