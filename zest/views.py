from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from zest.models import Pid,Tid
from zest.forms import Sign_up_form, log_in_form
from . forms import Generate_Pid_form
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
# Create your views here.

#signup
def signup(request):
  if request.method == 'POST':
    fm = Sign_up_form(request.POST)
    if fm.is_valid():
      fm.save()
      messages.success(request, 'Conratulations!! Now You are An Aurthor')
  else: 
    fm = Sign_up_form()
  return render(request,'zest/signup.html', {'form': fm})

#login
def log_in(request):
  if not request.user.is_authenticated:
    if request.method == 'POST':
      fm = log_in_form(request=request, data=request.POST)
      if fm.is_valid():
        uname = fm.cleaned_data['username']
        upass = fm.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        try:
          group = user.groups.get()
        except Exception as e:
          messages.error(request, 'You are not allowed to visit')
          return HttpResponseRedirect('/zest/login')  
        if not str(user.groups.get()) == 'rc_member' or request.user.is_superuser:
          messages.error(request, 'You are not allowed to visit')
          return HttpResponseRedirect('/zest/login')
        if user is not None:
          login(request, user)
          nm = request.user.username
          return HttpResponseRedirect('/zest/home',)
    else:  
      fm = log_in_form()
    return render(request,'zest/login.html', {'form':fm})
  else:
    return HttpResponseRedirect('/zest/login')

#logout
def log_out(request):
  logout(request)
  messages.error(request,'Logout Successfully !!')
  return HttpResponseRedirect('/zest/login/')

@login_required(login_url='/zest/login/')
def home(request):
  return render(request,'zest/home.html')

@login_required(login_url='/zest/login/')
def generate_pid(request):
  if request.method == "POST":
    fm = Generate_Pid_form(request.POST)
    if fm.is_valid():
      name = fm.cleaned_data['name']
      college_name = fm.cleaned_data['college_name']
      roll_no = fm.cleaned_data['roll_no']
      batch = fm.cleaned_data['batch']
      course = fm.cleaned_data['course']
      branch = fm.cleaned_data['branch']
      phone = fm.cleaned_data['phone']
      current_user = request.user
      pid = Pid(name=name,college_name=college_name,roll_no=roll_no,batch=batch,course=course,branch=branch,phone=phone,generated_by=current_user)
      pid.save()
      return HttpResponseRedirect('/zest/search_pid/{0}'.format(roll_no))
  else:
    fm = Generate_Pid_form()
  return render(request,'zest/generate_pid.html', {'form':fm})

@login_required(login_url='/zest/login/')
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

@login_required(login_url='/zest/login/')
def search_pid_by_roll(request, roll_no):
  if roll_no:
    pid  = Pid.objects.filter(roll_no=roll_no)[0]
    return render(request,'zest/pid_info.html', {'pid':pid})
      
@login_required(login_url='/zest/login/')
def generate_tid(request):
  tid = Tid()
  tid.save()
  return HttpResponseRedirect('/zest/add_pid_in_tid/{0}'.format(tid.id))

@login_required(login_url='/zest/login/')
def add_pid_in_tid(request,tid):
  tid_obj = Tid.objects.get(id=tid)
  if request.method == "POST":
    pid1 = request.POST.get('pid',False)
    tid_obj.pid.add(pid1)
    return render(request,'zest/tid_info.html',{'tid_obj':tid_obj})
  else:    
    return render(request,'zest/tid_info.html',{'tid_obj':tid_obj})
