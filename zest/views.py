from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from zest.models import Pid 
from . forms import Generate_Pid_form
# Create your views here.
def home(request):
  return render(request,'zest/home.html')

def generate_pid(request):
  if request.method == "POST":
    fm = Generate_Pid_form(request.POST)
    if fm.is_valid():
      fm.save()
      roll_no = fm.cleaned_data['roll_no']
      return HttpResponseRedirect('/zest/search_pid/{0}'.format(roll_no))
  else:
    fm = Generate_Pid_form()
  return render(request,'zest/generate_pid.html', {'form':fm})

def search_pid(request):
  roll_no = request.POST.get('roll_no', False)
  if roll_no:
    try:
      pid  = Pid.objects.filter(roll_no=roll_no)[0]
      if not pid:
        messages.error(request, 'Either Roll Number is incorrect or it is not registered.')
      return render(request,'zest/pid_info.html', {'pid':pid})
    except Exception as e:
      messages.error(request, 'Either Roll Number is incorrect or it is not registered.')
      return render(request,'zest/pid_info.html',)     
  else:
    messages.error(request, 'Please Enter Roll Number')
    return render(request,'zest/pid_info.html',)

def search_pid_by_roll(request, roll_no):
  if roll_no:
      pid  = Pid.objects.filter(roll_no=roll_no)[0]
      return render(request,'zest/pid_info.html', {'pid':pid})
      
