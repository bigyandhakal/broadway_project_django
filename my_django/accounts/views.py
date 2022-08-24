from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import User
from accounts.models import User
from jobs.models import Job
from jobseekers.models import Jobseeker

from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from rest_framework import permissions, status
from rest_framework import views
from rest_framework.response import Response
from . import serializers

from organizations.models import Category, Organizations, OrgUser
# Create your views here.


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def register_user(request):
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        em = request.POST['email']
        un = request.POST['username']
        pw = make_password(request.POST['password'])

        ob = request.POST['objective']
        qf = request.POST['qualification']
        tr = request.POST['training']
        sk = request.POST['skills']
        ex = request.POST['experience']
        cv = request.FILES['cv']
        im = request.FILES['image']

        user = User(first_name=fn, last_name=ln,
                    email=em, username=un, password=pw)
        user.save()

        js = Jobseeker(user=user, objective=ob, qualification=qf,
                       training=tr, skills=sk, experience=ex, cv=cv, image=im)
        js.save()

        # org = Organizations()
        # org.save()

        # orgusr = OrgUser(user=user, org=org)
        # orgusr.save()

        messages.success(request, 'Account has been created successfully!!')

        return redirect('login')

    messages.error(request, 'Invalid Access')
    return redirect('register')


def user_login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']

        user = auth.authenticate(username=un, password=pw)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('home')
        else:
            messages.error(request, 'Wrong Credentials Try again!!')
            return redirect('login')

    messages.error(request, 'Invalid access')
    return redirect('login')


def org_register(request):
    categories = Category.objects.filter(status=True)
    return render(request, 'organization_register.html', {'categories': categories})


def register_org(request):
    if request.method == 'POST':
        on = request.POST['orgname']
        cat = request.POST['category']
        ad = request.POST['address']
        cat = request.POST['category']
        estd = request.POST['estd']
        om = request.POST['omail']
        ph = request.POST['phone']
        dt = request.POST['details']
        lg = request.FILES['logo']

        fn = request.POST['fname']
        ln = request.POST['lname']
        em = request.POST['email']
        un = request.POST['username']
        pw = make_password(request.POST['password'])

        user = User(first_name=fn, last_name=ln,
                    email=em, username=un, password=pw)
        user.save()

        org = Organizations(category_id=cat, name=on, address=ad,
                            estd=estd, email=om, phone=ph, details=dt, logo=lg)
        org.save()

        orgusr = OrgUser(user=user, org=org)
        orgusr.save()

        messages.success(
            request, 'Organization account has been created successfully!!')
        return redirect('login')

    messages.error(request, 'Invalid Access')
    return redirect('organization_register')


def post_job(request):
    organization = Organizations.objects.filter(status=True)
    return render(request, 'job_post.html', {'organization': organization})


def job_post(request):
    if request.method == 'POST':
        ti = request.POST['jtitle']
        ty = request.POST['type']
        cat = request.POST['category']
        leve = request.POST['level']
        de = request.POST['descp']
        req = request.POST['requirement']
        exp = request.POST['experience']
        sk = request.POST['siklls']
        res = request.POST['respo']
        vac = request.POST['vacancy']
        sal = request.POST['salary']
        dead = request.POST['deadline']
        org = request.POST['organization']

        job = Job(title=ti, type=ty, category=cat, level=leve, description=de, requirements=req,
                  experience=exp, skills=sk, responsibilities=res, no_of_vacancy=vac, salary=sal, deadline=dead, organization=org)

        job.save()
        messages.success(request, 'Job posted with sucess!!')
        return redirect('jobs')

    messages.error(request, 'Cannot post job')
    return redirect('jobs')


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out sucessfully')
    return redirect('home')


@login_required
def profile(request):
    if request.user.is_staff:
        messages.warning(request, 'This page is not applicable.')
        return redirect('home')
    elif request.user.role == 'Employee':
        jobseeker = Jobseeker.objects.get(user=request.user)
        return render(request, 'profile.html', {'js': jobseeker})
    elif request.user.role == 'Employer':
        orguser = OrgUser.objects.get(user=request.user)
        organization = Organizations.objects.get(id=orguser.org_id)
        return render(request, 'profile.html', {'org': organization})
    else:
        messages.warning(request, 'This page is not applicable.')
        return redirect('home')

# login_required message show research


def update_profile(request):
    fn = request.POST['fname']
    ln = request.POST['lname']
    em = request.POST['email']
    un = request.POST['username']
    pw = request.POST['password']

    ob = request.POST['objective']
    qf = request.POST['qualification']
    tr = request.POST['training']
    sk = request.POST['skills']
    ex = request.POST['experience']
    cv = request.FILES['cv']
    im = request.FILES['image']

    user = request.user
    user.first_name = fn
    user.last_name = ln
    user.email = em
    if user.password != pw:
        user.password = make_password(pw)
    user.save()

    jobseeker = Jobseeker.objects.get(user=request.user)
    jobseeker.objective = ob
    jobseeker.save()


class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data,
                                                 context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        auth.login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)
