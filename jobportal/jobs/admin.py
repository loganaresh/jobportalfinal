from django.contrib import admin
from .models import Job, Applicant

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'job_type')
    list_filter = ('job_type',)
    search_fields = ('title',)

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'email', 'phone', 'applied_on')
    list_filter = ('job', 'applied_on')
    search_fields = ('name', 'email', 'phone')

    readonly_fields = ('name', 'email', 'phone', 'resume', 'job', 'applied_on')

    def has_change_permission(self, request, obj=None):
        if obj:
            return False
        return True


    def has_delete_permission(self, request, obj=None):
        return True
    def has_add_permission(self, request):
        return False
