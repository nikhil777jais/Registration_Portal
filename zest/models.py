from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
def validate_phone(value):
  if len(str(value)) == 10:
    return value
  else:
    raise ValidationError("Invalid Mobile No")

COLLEGE_CHOICES = (
        ('SRMS CET', 'SRMS CET'),
        ('SRMS CERT', 'SRMS UNNAO'),
        ('SRMS UNNAO', 'SRMS UNNAO'),
        ('SRMS IMS', 'SRMS IMS'),
        ('SRMS NURSING', 'SRMS NURSING'),
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
class Pid(models.Model):
  name = models.CharField(max_length=50, help_text='Enter Name')
  college_name = CharField(choices=COLLEGE_CHOICES, max_length=100, help_text='Select College')
  roll_no = models.IntegerField(unique=True)
  batch = models.CharField(choices=BATCH_CHOICES, max_length=25, help_text='Select Batch')
  course = models.CharField(choices=COURSE_CHOICES, max_length=25, help_text='Select Course')
  branch = models.CharField(choices=BRANCH_CHOICES, max_length=50, help_text='Select Branch')
  phone = models.IntegerField(help_text='Enter Mobile No',validators =[validate_phone])
  date_joined = models.DateTimeField(default=timezone.now)
  
