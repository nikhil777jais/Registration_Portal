from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from zest.models import Pid, Team_Event,Tid, Individual_Event, Team_Event
from zest.forms import Sign_up_form, log_in_form, Generate_Pid_form, Generate_Tid_form
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
# Create your views here.

#signup
def signup(request):
  if request.method == 'POST':
    fm = Sign_up_form(request.POST)
    if fm.is_valid():
      fm.save()
      messages.success(request, 'Conratulations!!')
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
        if not str(user.groups.get()) == 'rc_member':
          messages.error(request, 'You are not allowed to visit')
          return HttpResponseRedirect('/zest/login')
        if user is not None:
          login(request, user)
          if request.user.is_staff:
            return HttpResponseRedirect('/zest/event_summary/')
          return HttpResponseRedirect('/zest/home')
    else:  
      fm = log_in_form()
    return render(request,'zest/login.html', {'form':fm})
  else:
    return HttpResponseRedirect('/zest/login')

#logout
def log_out(request):
  logout(request)
  messages.error(request,'Logged Out Successfully !!')
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
      gender = fm.cleaned_data['gender']
      phone = fm.cleaned_data['phone']
      current_user = request.user
      pid = Pid(name=name,college_name=college_name,roll_no=roll_no,batch=batch,course=course,branch=branch,phone=phone,generated_by=current_user, gender=gender)
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
        messages.error(request, 'Either Roll Number is incorrect or is not registered.')
      return render(request,'zest/pid_info.html', {'pid':pid})
    except Exception as e:
      messages.error(request, 'Either Roll Number is incorrect or is not registered.')
      return render(request,'zest/pid_info.html',)     
  else:
    return render(request,'zest/pid_info.html',)

@login_required(login_url='/zest/login/')
def search_pid_by_roll(request, roll_no):
  if roll_no:
    pid  = Pid.objects.filter(roll_no=roll_no)[0]
    return render(request,'zest/pid_info.html', {'pid':pid})
      
@login_required(login_url='/zest/login/')
def generate_tid(request):
  if request.method == "POST":
    fm = Generate_Tid_form(request.POST)
    if fm.is_valid():
      college_name = fm.cleaned_data['college_name']
      current_user = request.user
      tid = Tid(college_name=college_name, generated_by=current_user)
      tid.save()
      return HttpResponseRedirect('/zest/add_pid_in_tid/{0}'.format(tid.id))
  else:
    fm =Generate_Tid_form()
    return render(request, 'zest/generate_tid.html', {'form':fm})

@login_required(login_url='/zest/login/')
def search_tid(request):
  fm = Generate_Tid_form()
  tid = request.POST.get('tid', False)
  if tid:
    try:
      tid_obj  = Tid.objects.get(id=tid)
      return render(request,'zest/tid_info.html', {'tid_obj':tid_obj})
    except Exception as e:
      messages.error(request, 'Either tid is incorrect or is not registered.')
      return render(request,'zest/generate_tid.html',{'form':fm})     
  else:
    return render(request,'zest/generate_tid.html',{'form':fm})

@login_required(login_url='/zest/login/')
def add_pid_in_tid(request,tid=None):
  tid_obj = Tid.objects.get(id=tid)
  if request.method == "POST":
    pid1 = request.POST.get('pid',False)
    if pid1:
      try:
        tid_obj.pid.add(pid1)
        return render(request,'zest/tid_info.html',{'tid_obj':tid_obj})
      except Exception as e:
        messages.error(request, 'Enter correct PID')
        return render(request,'zest/tid_info.html',{'tid_obj':tid_obj})
    else:
      messages.error(request, 'Enter PID to be add')
      return render(request,'zest/tid_info.html',{'tid_obj':tid_obj})
  else:    
    return render(request,'zest/tid_info.html',{'tid_obj':tid_obj})

@login_required(login_url='/zest/login/')
def register_event(request):
  return render(request,'zest/register_event.html')

@login_required(login_url='/zest/login/')
def add_event_in_pid(request):
  event_name = request.POST.get('event_name',False)
  pid = request.POST.get('pid',False)
  if pid:
    try:
      pid_obj = Pid.objects.get(id=pid)
      individual_event_obj = Individual_Event.objects.filter(event_name=event_name)[0]
      individual_event_obj.pid.add(pid_obj)
      individual_event_obj.save()
      return render(request, "zest/pid_info.html",{'pid':pid_obj})
    except Exception as e:
      messages.error(request, 'Either pid is incorrect or is not registered.')
      return render(request,'zest/register_event.html')
  else:   
    return render(request,'zest/register_event.html')

@login_required(login_url='/zest/login/')
def add_event_in_tid(request):
  event_name = request.POST.get('event_name',False)
  tid = request.POST.get('tid',False)
  try:
    tid_obj = Tid.objects.get(id=tid)
    pid_count = tid_obj.pid_count
    if event_name == 'GROUP DANCE':
      if pid_count < 7 or pid_count > 25:
        messages.error(request,'Team Member shuold be between 7 to 25')
        return render(request,'zest/register_event.html')
    elif event_name == 'DUET DANCE':
      if pid_count != 2:
        messages.error(request,'Team should have only 2 member')
        return render(request,'zest/register_event.html')
    elif event_name == 'MULTISCENE':
      if pid_count < 8 or pid_count > 20:
        messages.error(request,'Team Member shuold be between 8 to 20')
        return render(request,'zest/register_event.html')
    elif event_name == 'STREET PLAY':
      if pid_count < 10 or pid_count > 20:
        messages.error(request,'Team Member shuold be between 10 to 20')
        return render(request,'zest/register_event.html')
    elif event_name == 'MIME':
      if pid_count < 6 or pid_count > 15:
        messages.error(request,'Team Member shuold be between 6 to 15')
        return render(request,'zest/register_event.html')
    elif event_name == 'GRATIS':
      if pid_count != 2:
        messages.error(request,'Team should have only 2 member')
        return render(request,'zest/register_event.html')
    elif event_name == 'SITUATIONAL ANTAKSHRI':
      if pid_count != 4:
        messages.error(request,'Team should have only 4 member')
        return render(request,'zest/register_event.html')
    elif event_name == 'DUMB CHARADES':
      if pid_count != 2:
        messages.error(request,'Team should have only 4 member')
        return render(request,'zest/register_event.html')
    elif event_name == 'RANGOLI':
      if pid_count != 2:
        messages.error(request,'Team should have only 2 member')
        return render(request,'zest/register_event.html')
    elif event_name == 'DUET SONG':
      if pid_count != 2:
        messages.error(request,'Team should have only 2 member')
        return render(request,'zest/register_event.html')
    # only 6 teams allowed in FCFS
    elif event_name == 'BATTLE OF BANDS':
      team_event_obj = Team_Event.objects.filter(event_name=event_name)[0]
      if team_event_obj.tid_count >= 6:
        messages.error(request,'Registration closed for ths event')
        return render(request,'zest/register_event.html')  
      elif pid_count < 4 or pid_count > 8:
        messages.error(request,'Team Member shuold be between 4 to 8')
        return render(request,'zest/register_event.html')
    # one team form one college   
    elif event_name == 'STORY RECITATION':
      if pid_count != 4:
        messages.error(request,'Team should have only 2 member')
        return render(request,'zest/register_event.html')
    elif event_name == 'MIME':
      if pid_count < 6 and pid_count > 15:
        messages.error(request,'Team Member shuold be between 6 to 15')
        return render(request,'zest/register_event.html')
  except:
    messages.error(request, 'Either tid is incorrect or it is not registered.')
    return render(request,'zest/register_event.html')

  if tid_obj.tid_event.all():
    messages.error(request, 'This team is already registered')
    return render(request,'zest/register_event.html')
  if tid:
    try:
      team_event_obj = Team_Event.objects.filter(event_name=event_name)[0]
      team_event_obj.tid.add(tid_obj)
      team_event_obj.save()
      return render(request, "zest/tid_info.html",{'tid_obj':tid_obj})
    except Exception as e:
      messages.error(request, 'Either tid is incorrect or is not registered.')
      return render(request,'zest/register_event.html')
  else:   
    return render(request,'zest/register_event.html')

@login_required(login_url='/zest/login/')
def event_summary(request):
  i_events = Individual_Event.objects.all()
  t_events = Team_Event.objects.all()
  return render(request,'zest/event_summary.html', {'i_events': i_events, 't_events':t_events})

@login_required(login_url='/zest/login/')
def event_details(request,id):
  individual_event_obj =Individual_Event.objects.get(id=id)
  pids = individual_event_obj.pid.all()
  return render(request,'zest/event_details.html', {'pids': pids})
  
@login_required(login_url='/zest/login/')
def t_event_details(request,id):
  team_event_obj = Team_Event.objects.get(id=id)
  tids = team_event_obj.tid.all()
  return render(request,'zest/t_event_details.html', {'tids': tids})
  
   
