# Generated by Django 3.2.9 on 2021-11-18 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zest', '0002_alter_pid_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, default=31000, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.ManyToManyField(blank=True, related_name='pids', to='zest.Pid')),
            ],
        ),
    ]
