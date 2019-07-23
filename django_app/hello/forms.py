# -*- coding: utf-8 -*-
from django import forms
from .models import Friend

class FriendForm(forms.ModelForm):
    class Meta:
        model=Friend
        fields=['name','mail','gender','age','birthday']
        
    #name=forms.CharField(label='Name')
    #mail=forms.EmailField(label='Email')
    #gender=forms.BooleanField(label='Gender', required=False)
    #ge=forms.IntegerField(label='Age')
    #birthday=forms.DateField(label='Birth')

class FindForm(forms.Form):
    find=forms.CharField(label='Find', required=False)
    
class CheckForm(forms.Form):
    str=forms.CharField(label='Name')
    