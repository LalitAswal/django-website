# Generated by Django 3.0.6 on 2020-05-22 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btech', '0016_auto_20200522_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='subjects',
            new_name='subject1',
        ),
        migrations.AddField(
            model_name='subject',
            name='subject2',
            field=models.CharField(blank=True, max_length=208),
        ),
        migrations.AddField(
            model_name='subject',
            name='subject3',
            field=models.CharField(blank=True, max_length=208),
        ),
        migrations.AddField(
            model_name='subject',
            name='subject4',
            field=models.CharField(blank=True, max_length=208),
        ),
        migrations.AddField(
            model_name='subject',
            name='subject5',
            field=models.CharField(blank=True, max_length=208),
        ),
        migrations.AddField(
            model_name='subject',
            name='subject6',
            field=models.CharField(blank=True, max_length=208),
        ),
    ]
