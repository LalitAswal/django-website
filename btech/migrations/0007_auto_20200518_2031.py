# Generated by Django 3.0.6 on 2020-05-18 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('btech', '0006_year_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='year',
            old_name='subject',
            new_name='sub',
        ),
    ]
