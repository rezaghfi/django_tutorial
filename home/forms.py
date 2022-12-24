from django import forms
from .models import Todo
class TodoCreateForm(forms.Form):
    title = forms.CharField(max_length=100, label='onvam')
    body = forms.CharField()
    created = forms.DateTimeField()

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        # fields = ['title', 'body', 'created']
        fields = '__all__'

