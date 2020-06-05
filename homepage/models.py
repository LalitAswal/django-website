from django.db import models

# Create your models here.


class QuestionPaper(models.Model):
    subject = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='')