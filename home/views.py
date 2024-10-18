from django.shortcuts import render
from job.models import job
# Create your views here.
def home (request):
    jobs =job.objects.all()
    

    return render(request, 'home.html',{'job':jobs})