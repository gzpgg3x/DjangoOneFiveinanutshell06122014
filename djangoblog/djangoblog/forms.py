# -*- encoding: utf-8 -*-
from django import forms
 
class SearchForm(forms.Form):
  query = forms.CharField(min_length=3, required=False)
