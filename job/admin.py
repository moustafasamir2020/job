from django.contrib import admin
from . models import job , category
# Register your models here.
class JobAdmin(admin.ModelAdmin):
    
    list_display = ['title','id']

admin.site.register(job,JobAdmin)
admin.site.register(category)