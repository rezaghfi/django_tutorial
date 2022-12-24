from django import forms
from .models import Todo
class TodoCreateForm(forms.Form):
    title = forms.CharField(max_length=100, label='عنوان کار:')
    body = forms.CharField(label="متن کار:")
    created = forms.DateTimeField(label="تاریخ ایجاد:")

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        # fields = ['title', 'body', 'created']
        labels = {
            "title": "عنوان کار::",
            "body":"متن کار:",
            "created":"تاریخ ایجاد:"
        }
        fields = '__all__'

