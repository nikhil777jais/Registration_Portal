# Generated by Django 3.2.9 on 2021-11-20 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zest', '0002_auto_20211120_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tid',
            name='id',
            field=models.BigAutoField(auto_created=True, default=31000, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]