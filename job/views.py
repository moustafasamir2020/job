from django.shortcuts import render
from . models import job
# Create your views here.
def job_list(request):
    jobs =job.objects.all()
    context = {'jobs':jobs}
    return render (request,'job_list.html',context)  

def job_detail(request,id):
    job_detail=job.objects.get(id=id)
    context={'job':job_detail}


    return render (request,'job_details.html',context)