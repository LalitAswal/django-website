from django.shortcuts import render
from .models import Subject
# Create your views here.


def sub(request):
    subject = Subject.objects.all()
    return render(request, 'btech/btech.html',  {'subject': subject})

                  
                  


