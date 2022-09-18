
from django.forms import ModelForm
from .models import Topic
from django import forms


class NewTopicForm(ModelForm):
    message = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = Topic
        fields = ['subject', 'message']

