from django import forms
from .models import Topic, Post


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(max_length=4000, help_text='Max Length is 4000', widget=forms.Textarea(attrs={'rows': 5}))

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message']
        help_texts = {'message': 'Max Length is 4000'}
        widgets = {'message': forms.Textarea(attrs={'rows': 5})}
