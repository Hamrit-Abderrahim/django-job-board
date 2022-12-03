from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm, JobForm


# Create your views here.s


def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 3)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'jobs': page_obj}
    return render(request, 'job/jobs_list.html', context)


def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myForm = form.save(commit=False)
            myForm.job = job_detail
            myForm = form.save()
    else:
        form = ApplyForm()

    context = {'job': job_detail, 'form': form}

    return render(request, 'job/job_details.html', context)


def add_job(request):

    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myForm = form.save(commit=False)
            myForm.owner = request.user
            myForm.save(

            )
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()

    return render(request, 'job/add_job.html', {'form1': form})
