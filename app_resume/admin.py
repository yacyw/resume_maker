from django.contrib import admin

from app_resume.models import Resume , WorkExprience

# Register your models here.

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user','job_title','about','field_type',)
    list_editable =('job_title',)
    search_fields=('user__username','user__first_name','user__last_name')


admin.site.register(Resume, ResumeAdmin )

class WorkExprienceAdmin(admin.ModelAdmin):
    list_display=('title','resume')
    list_filter=('resume',)

admin.site.register(WorkExprience,WorkExprienceAdmin)

