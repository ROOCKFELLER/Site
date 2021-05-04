from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError
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