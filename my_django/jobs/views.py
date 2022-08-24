from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect
from jobs.models import Job
from django.contrib import messages
from organizations.models import Category, OrgUser, Organizations
# Create your views here.


def show_jobs(request):
    jobs = Job.objects.all()
    # qry = """ SELECT category_id, count(*) FROM jobs GROUP BY category_id """
    curosr = connection.cursor()
    curosr.execute(
        'SELECT category_id, count(*) FROM jobs_job GROUP BY category_id')
    counts = curosr.fetchall()
    return render(request, 'jobs.html', {'jobs': jobs, 'counts': counts})


def show_single_job(request, id):
    # job = Job.objects.filter(id= id)
    job = Job.objects.get(pk=id)  # for primary key
    # return HttpResponse(job.title)
    return render(request, 'job_details.html', {'job': job})


def show_job_by_category(request, cid):
    jobs = Job.objects.filter(category_id=cid)
    return render(request, 'jobs.html', {'jobs': jobs})


def show_searched_jobs(request):
    # if request.method == 'POST':
    # key = request.POST['key']
    key = request.GET['key']
    jobs = Job.objects.filter(title__icontains=key)
    return render(request, 'jobs.html', {'jobs': jobs})


def post_job(request):
    organization = Organizations.objects.filter(status=True)
    category = Category.objects.all()
    return render(request, 'job_post.html', {'organization': organization,'category': category})


def job_post(request):
    if request.method == 'POST':
        ti = request.POST['jtitle']
        ty = request.POST['type']
        cat = request.POST['category']
        leve = request.POST['level']
        de = request.POST['descp']
        req = request.POST['req']
        exp = request.POST['experience']
        sk = request.POST['skills']
        res = request.POST['respo']
        vac = request.POST['vacancy']
        sal = request.POST['salary']
        dead = request.POST['deadline']
        org = OrgUser.objects.get(user=request.user)

        job = Job(title=ti, type=ty, category_id=cat, level=leve, description=de, requirement=req,
                  experience=exp, skills=sk, responsibilities=res, no_of_vacancy=vac, salary=sal, deadline=dead, organization=org.org)

        job.save()
        messages.success(request, 'Job posted with success!!')
        return redirect('jobs')

    messages.error(request, 'Cannot post job')
    return redirect('jobs')
