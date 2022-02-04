from cProfile import label
from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Comment, Post

class NewComment(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('name', 'email', 'body')
        



class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label = 'العنوان')
    content = forms.CharField(label = 'نص التدوينة', widget= forms.Textarea)
    
    class Meta():
        model = Post
        fields = ('title', 'content')