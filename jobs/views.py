from django.shortcuts import render
#to get all the objects from the models to here so that it can be passed to html file
from .models import Job

def home(request):
    jobs = Job.objects
    return render(request,'jobs\home.html', {'Jobs':jobs})
