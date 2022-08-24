from django.contrib import admin
from information.models import Section, Information
# Register your models here.

class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')

class InfoAdmin(admin.ModelAdmin):
    list_display = ('section','title','details','status')

admin.site.register(Section, SectionAdmin)
admin.site.register(Information, InfoAdmin)