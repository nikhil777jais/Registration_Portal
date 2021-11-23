from django.db.models import fields
from django.db.models.base import Model
from django.forms import widgets
from . models import Pid, Tid
from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class Sign_up_form(UserCreationForm):
  password1 = forms.CharField(widget=widgets.PasswordInput(attrs={'class':'form-control'}),label='Password' )
  password2 = forms.CharField(widget=widgets.PasswordInput(attrs={'class':'form-control'}),label='Confirm Password')
  class Meta:
    model = User
    fields = ['username','email', 'first_name', 'last_name']
    
    widgets = {
            'username': forms.TextInput(attrs={'class':'form-control',},),
            'email': forms.EmailInput(attrs={'class':'form-control'},),
            'first_name': forms.TextInput(attrs={'class':'form-control'},),
            'last_name': forms.TextInput(attrs={'class':'form-control'},),
    }
class log_in_form(AuthenticationForm):
  username = forms.CharField(widget=widgets.TextInput(attrs={'class':'form-control'}))
  password = forms.CharField(widget=widgets.PasswordInput(attrs={'class':'form-control'}))

class Generate_Pid_form(forms.ModelForm):
  class Meta:
    model = Pid
    fields = ['name', 'college_name','roll_no','batch','course','branch','gender','phone']
    widgets = {
      'name': forms.TextInput(attrs={'class':'form-control'}),
      'college_name': forms.Select(attrs={'class':'form-control'}),
      'roll_no': forms.NumberInput(attrs={'class':'form-control'}),
      'batch': forms.Select(attrs={'class':'form-control'}),
      'course': forms.Select(attrs={'class':'form-control'}),
      'branch': forms.Select(attrs={'class':'form-control'}),
      'gender': forms.Select(attrs={'class':'form-control'}),
      'phone': forms.NumberInput(attrs={'class':'form-control'}),
      }
    

class Generate_Tid_form(forms.ModelForm):
  class Meta:
    model = Tid
    fields = ['college_name']
    widgets = {
      'college_name': forms.Select(attrs={'class':'form-control'}),
    }
    labels = {'college_name':'College Name'}