from django.contrib import admin
from . models import Pid, Tid, Individual_Event, Team_Event

@admin.register(Pid)
class PidAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'roll_no','generated_by']

@admin.register(Tid)
class TidAdmin(admin.ModelAdmin):
    list_display = ['id','pids','generated_by']

@admin.register(Individual_Event)
class Individual_EventAdmin(admin.ModelAdmin):
    list_display = ['id','event_name','pids']

@admin.register(Team_Event)
class Team_EventAdmin(admin.ModelAdmin):
    list_display = ['id','event_name','tids']