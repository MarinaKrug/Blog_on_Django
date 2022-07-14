from django.forms import ModelForm, Textarea

from blogs.models import BlogPost


class EntryForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','text']
        labels = {'title':'Введите заголовок статьи:'}
        widgets = {'text': Textarea(attrs={'cols': 120})}