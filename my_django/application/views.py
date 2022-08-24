from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from application.models import Application
from jobs.models import Job
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jobseekers.models import Jobseeker

from organizations.models import OrgUser, Organizations
# Create your views here.


@login_required
def apply(request, jid):
    if request.user.is_staff:
        messages.warning(request, 'This url is not applicable for your role')
    elif request.user.role == 'Employee':
        job = Job.objects.get(id=jid)
        app = Application.objects.filter(user=request.user).filter(job=job)
        if app:
            messages.success(request, 'You have already applied for the job')
            return redirect('jobs')
        app = Application(user=request.user, job=job, status='Applied')
        # app = Application(user_id = request.userid, job=jid, status='applied' )
        app.save()
        messages.success(request, 'You have applied for the job')
    else:
        messages.warning(request, 'This url is not applicable for your role')
    return redirect('jobs')


@login_required
def applied_jobs(request):
    app = Application.objects.filter(user=request.user)
    # return HttpResponse()
    return render(request, 'applied_jobs.html', {'application':app})


@login_required
def posted_jobs(request):
    orguser = OrgUser.objects.get(user=request.user)
    org = Organizations.objects.get(id=orguser.org_id)
    # return HttpResponse(org)
    jobs = Job.objects.filter(organization=org)
    return render(request, 'org_posted_job.html', {'posted':jobs})


@login_required
def application_by_job(request, jid):
    applications = Application.objects.filter(job_id=jid)
    users = Application.objects.filter(job_id=jid).values_list('user_id')
    jobseeker = Jobseeker.objects.filter(user__in=users)
    for i in range (len(applications)):
        applications[i].js = jobseeker[i]

    return render(request, 'application_by_job.html', {'byjob':applications})



@login_required
def change_status(request, id):
    if request.method == 'POST':
        app = Application.objects.get(id=id)
        app.status = request.POST['status']
        app.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))