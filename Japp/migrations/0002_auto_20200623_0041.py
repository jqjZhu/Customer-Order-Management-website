# Generated by Django 3.0.7 on 2020-06-23 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Japp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='time_create',
            new_name='time_created',
        ),
    ]