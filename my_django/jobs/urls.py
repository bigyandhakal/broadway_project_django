from django.urls import path
from jobs import views

urlpatterns= [
    path('', views.show_jobs, name='jobs'),
    path('single/<id>', views.show_single_job,name='single_job'),
    path('categories/<cid>', views.show_job_by_category,name='categoried_jobs'),
    path('search', views.show_searched_jobs,name='search'),
    path('post_job', views.post_job, name='post_job'),
    path('job_post', views.job_post, name='job_post'),
]