# Generated by Django 3.0.6 on 2020-05-18 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('btech', '0008_subject_steam'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='Steam',
            new_name='steams',
        ),
    ]
