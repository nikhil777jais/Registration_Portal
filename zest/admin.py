from django.contrib import admin
from . models import Pid, Tid

@admin.register(Pid)
class PidAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'roll_no',]

@admin.register(Tid)
class TidAdmin(admin.ModelAdmin):
    list_display = ['id','pids']