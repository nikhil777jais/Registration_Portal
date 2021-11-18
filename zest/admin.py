from django.contrib import admin
from . models import Pid

@admin.register(Pid)
class PidAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'roll_no',]