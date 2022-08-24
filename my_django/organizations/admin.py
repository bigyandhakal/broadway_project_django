from django.contrib import admin

from organizations.models import Category, OrgUser, Organizations

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'details', 'status')

class OrgAdmin(admin.ModelAdmin):
    list_display = ('name','estd','address','category','status')

admin.site.register(Organizations, OrgAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(OrgUser)