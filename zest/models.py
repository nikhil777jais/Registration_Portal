from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# Create your models here.
def validate_phone(value):
  if len(str(value)) == 10:
    return value
  else:
    raise ValidationError("Invalid Mobile Number")

def validate_name(value):
  inputs = list(map(str,value.split()))
  for input in inputs:
    if not input.isalpha():
      raise ValidationError("Enter Character Only")
  else:
    return value


COLLEGE_CHOICES =	(
	('SRMS CET', 'SRMS CET'),
  ('SRMS CETR', 'SRMS CETR'),
  ('SRMS UNNAO', 'SRMS UNNAO'),
  ('SRMS IMS', 'SRMS IMS'),
  ('SRMS NURSING', 'SRMS NURSING'),
  ('OTHER', 'OTHER'),
)
COURSE_CHOICES = (
  ('B.Tech.', 'B.Tech.'),
  ('M.Tech.', 'M.Tech.'),
  ('B.Pharma', 'B.Pharma'),
  ('M.Pharma', 'M.Pharma'),
  ('MBA', 'MBA'),
)
BRANCH_CHOICES = (
	('CSE', 'CSE'),
	('IT', 'IT'),
	('EC', 'EC'),
	('EN', 'EN'),
	('ME', 'ME'),
	('NA', 'NA'),
)
BATCH_CHOICES = (
	('2021', '2021'),
	('2020', '2020'),
	('2019', '2019'),
	('2018', '2018'),
	('2017', '2017'),
)
GENDER_CHOICES = (
	('MALE', 'MALE'),
	('FEMALE', 'FEMALE'),
)
class Pid(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=50, help_text='Enter Name', validators=[validate_name])
    college_name = CharField(choices=COLLEGE_CHOICES, max_length=100, help_text='Select College')
    roll_no = models.BigIntegerField(unique=True)
    batch = models.CharField(choices=BATCH_CHOICES, max_length=25, help_text='Select Batch')
    course = models.CharField(choices=COURSE_CHOICES, max_length=25, help_text='Select Course')
    branch = models.CharField(choices=BRANCH_CHOICES, max_length=50, help_text='Select Branch')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, help_text='Select Gender')
    phone = models.BigIntegerField(help_text='Enter Mobile No',validators =[validate_phone])
    date_joined = models.DateTimeField(default=timezone.now)
    generated_by = models.ForeignKey(User, on_delete=models.PROTECT,related_name='gereted_pid')

    @property
    def tids(self):
    	return self.pids.all()

    @property
    def tids(self):
    	return self.pid_event.all() 

class Tid(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    college_name = CharField(choices=COLLEGE_CHOICES, max_length=100,  help_text='Select College')
    pid = models.ManyToManyField(Pid, blank=True, related_name= 'pids')
    generated_by = models.ForeignKey(User, on_delete=models.PROTECT,related_name='gereted_tid')

    @property
    def pid_count(self):
      return self.pid.count()

    def get_all_pid(self):
      return self.pid.all()

    def pids(self):
      return " , ".join([ str(p.id) for p in self.pid.all()])  
 
      
class Individual_Event(models.Model):
    event_name = CharField(max_length=100,  help_text='Enter Event Name',)
    event_venue = CharField(max_length=100,  help_text='Enter Event Venue',)
    event_time = models.DateTimeField(default=timezone.now)
    pid = models.ManyToManyField(Pid, blank=True, related_name= 'pid_event')
    
    @property
    def pid_count(self):
      return self.pid.count()

    def pids(self):
      return " , ".join([ str(p.id) for p in self.pid.all()])  
      
class Team_Event(models.Model):
    event_name = CharField(max_length=100,  help_text='Enter Event Name',)
    event_venue = CharField(max_length=100,  help_text='Enter Event Venue',default=None)
    event_time = models.DateTimeField(default=timezone.now)
    tid = models.ManyToManyField(Tid, blank=True, related_name= 'tid_event')

    @property
    def tid_count(self):
      return self.tid.count()

    def tids(self):
      return " , ".join([ str(t.id) for t in self.tid.all()])  
