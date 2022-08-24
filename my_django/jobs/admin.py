from django.contrib import admin

from jobs.models import Job

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'type','category','level','salary','organization')


admin.site.register(Job, JobAdmin)
