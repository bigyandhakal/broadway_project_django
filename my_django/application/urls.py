from django.urls import path

from application import views


urlpatterns = [
    path('apply/<jid>', views.apply, name='apply'),
    path('applied_jobs', views.applied_jobs, name='applied_jobs'),
    path('posted_jobs', views.posted_jobs, name='posted_jobs'),
    path('byjob/<jid>', views.application_by_job, name='application_by_job'),
    path('change_status/<id>', views.change_status, name='change_status'),
]