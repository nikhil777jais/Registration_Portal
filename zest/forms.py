from . models import Pid
from django import forms

class Generate_Pid_form(forms.ModelForm):
  class Meta:
    model = Pid
    fields = ['name', 'college_name','roll_no','batch','course','branch','phone']
    widgets = {
      'name': forms.TextInput(attrs={'class':'form-control'}),
      'college_name': forms.Select(attrs={'class':'form-control'}),
      'roll_no': forms.NumberInput(attrs={'class':'form-control'}),
      'batch': forms.Select(attrs={'class':'form-control'}),
      'course': forms.Select(attrs={'class':'form-control'}),
      'branch': forms.Select(attrs={'class':'form-control'}),
      'phone': forms.NumberInput(attrs={'class':'form-control'}),
      }
    labels = {'Name':'Full Name','college_name':'College Name','roll_no':'Roll Number','phone':'Contact Number'}