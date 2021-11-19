from django.contrib import admin
from . models import Pid, Tid, Individual_Event, Team_Event

@admin.register(Pid)
class PidAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'roll_no',]

@admin.register(Tid)
class TidAdmin(admin.ModelAdmin):
    list_display = ['id','pids']

@admin.register(Individual_Event)
class Individual_EventAdmin(admin.ModelAdmin):
    list_display = ['id','event_name','pid']

@admin.register(Team_Event)
class Team_EventAdmin(admin.ModelAdmin):
    list_display = ['id','event_name','tid']