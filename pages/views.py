from django.shortcuts import render
from .models import Trainee
from .scrapper import badgefetcher

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        cohort = request.POST['cohort']
        credly = request.POST['credly']

        new_trainee = Trainee(name=name, cohort=cohort, credly=credly)
        new_trainee.save()

    trainees = Trainee.objects.all()

    context = {
        'trainees': trainees
    }
    return render(request, 'index.html', context)

def cohort(request):
    name = request.GET['name']
    
    trainee = Trainee.objects.filter(name=name).values('credly')
    
    url = trainee[0]['credly']
    
    badges = badgefetcher(url)

    context = {
        'badges': badges
    }
    return render(request, 'cohort.html', context)