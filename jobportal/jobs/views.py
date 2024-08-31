from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect
from .models import Job, Applicant
from .forms import ApplicantForm, JobFilterForm

def job_list(request):
    jobs = Job.objects.all()


    job_type = request.GET.get('job_type')
    search_query = request.GET.get('search_query')

    if job_type:
        jobs = jobs.filter(job_type=job_type)
    
    if search_query:
        jobs = jobs.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))

    form = JobFilterForm(request.GET or None)
    
    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'form': form})
def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.job = job
            applicant.save()
            return HttpResponseRedirect('/jobs/')
    else:
        form = ApplicantForm()
    return render(request, 'jobs/job_detail.html', {'job': job, 'form': form})
