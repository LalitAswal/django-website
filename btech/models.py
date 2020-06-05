from django.db import models
from django.db.models import Model


# Create your models here.
class Subject(models.Model):
    SEMESTER = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th'),
        ('5th', '5th'),
        ('6th', '6th'),
        ('7th', '7th'),
        ('8th', '8th'),
    )

    STREAM = (
        ('CS', 'Computer Science'),
        ('CIVIL', 'Civil Engineering'),
        ('MECHANICAL', 'Mechanical Engineering'),
        ('ECE', 'Electrical and Communication Engineering'),
        ('EE', 'Electrical Engineering'),
             )
    stream = models.CharField(max_length=204, choices=STREAM, null=True)
    semester = models.CharField(max_length=204, choices=SEMESTER, null=True)
    subject1 = models.CharField(max_length=208,  blank=True)
    subject2 = models.CharField(max_length=208, blank=True)
    subject3 = models.CharField(max_length=208,  blank=True)
    subject4 = models.CharField(max_length=208,  blank=True)
    subject5 = models.CharField(max_length=208,  blank=True)
    subject6 = models.CharField(max_length=208, blank=True)

    def __str__(self):
        return '{} {} '.format(self.stream, self.semester)


class Year(models.Model):

    sub = models.CharField(Subject, max_length=208,  null=True)
    year12 = models.FileField(upload_to='', blank=True)
    year13 = models.FileField(upload_to='', blank=True)
    year14 = models.FileField(upload_to='', blank=True)
    year15 = models.FileField(upload_to='', blank=True)
    year16 = models.FileField(upload_to='', blank=True)
    year17 = models.FileField(upload_to='', blank=True)
    year18 = models.FileField(upload_to='', blank=True)

    def __str__(self):
        return str(self.sub)










