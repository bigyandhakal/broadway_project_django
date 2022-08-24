from django.contrib import admin

from jobseekers.models import Jobseeker

# Register your models here.

class JobseekerAdmin(admin.ModelAdmin):
    list_display = ('user', 'objective','qualification','status')


admin.site.register(Jobseeker, JobseekerAdmin)
