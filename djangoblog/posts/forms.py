# -*- encoding: utf-8 -*-
 
from django import forms
from posts.models import Commentary
 
class AddCommentaryForm(forms.ModelForm):
  class Meta:
    model = Commentary
    fields = ('author', 'content')
    # fields = ('post', 'content')
    # fields = ('owner', 'content')