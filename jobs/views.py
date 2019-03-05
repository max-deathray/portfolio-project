from django.shortcuts import render

# access items from the database
from .models import Job


def home(request):
    # this next line grabs all the jobs from the database
    jobs = Job.objects
    # then pass a diction to the render function
    return render(request, 'jobs/home.html', {'jobs': jobs})
