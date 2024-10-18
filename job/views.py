from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.urls import reverse
from . models import job
from . form import apply_form,Jobform
# Create your views here.
def job_list(request):
    jobs =job.objects.all()
    paginator = Paginator(jobs,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'jobs':page_obj,'job':jobs}
    return render (request,'job_list.html',context)  

def job_detail(request,slug):
    job_detail=job.objects.get(slug=slug)
    if request.method == 'POST':
        form = apply_form (request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job=job_detail
            myform.save()
            return redirect(reverse('job:job_list'))  

    else:
        form = apply_form ()


    context={'job':job_detail,'form':form}


    return render (request,'job_details.html',context)


def add_job (request):
    if request.method == 'POST':
        form = Jobform (request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('job:job_list'))  

    else:
        form = Jobform ()

    return render (request,'add_job.html',{'form1':form})