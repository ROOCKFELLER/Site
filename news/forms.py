from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label = 'Имя пользователя', widget = forms.TextInput(attrs= {'class': 'username', 'autocomplete': 'off'}))
    
    password = forms.CharField(label = 'Пароль', widget = forms.PasswordInput(attrs= {'class': 'password'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label = 'Имя пользователя', widget = forms.TextInput(attrs= {'class': 'username', 'autocomplete': 'off'}))

    email = forms.EmailField(label = 'E-mail', widget = forms.EmailInput(attrs= {'class': 'email'}))

    password1 = forms.CharField(label = 'Пароль', widget = forms.PasswordInput(attrs= {'class': 'password'}))
    password2 = forms.CharField(label = 'Подтверждения пароля', widget = forms.PasswordInput(attrs= {'class': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Введите название статьи...'}),
            'content': forms.Textarea(attrs={'placeholder':'Введите статью...', 'cols':'40','rows':'30'}),
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title