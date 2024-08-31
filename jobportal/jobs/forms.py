from django import forms
from .models import Applicant, Job

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['name', 'email', 'phone', 'resume']

class JobFilterForm(forms.Form):
    job_type = forms.ChoiceField(
        choices=[('', 'All')] + Job.JOB_TYPES,
        required=False,
        label="Job Type"
    )
    search_query = forms.CharField(
        max_length=100,
        required=False,
        label="Search"
    )