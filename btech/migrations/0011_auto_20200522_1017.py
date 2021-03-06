# Generated by Django 3.0.6 on 2020-05-22 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('btech', '0010_subject_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='subject',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='year',
            name='sub',
        ),
        migrations.AddField(
            model_name='year',
            name='sem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='btech.Semester'),
        ),
    ]
