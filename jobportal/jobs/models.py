import os
from django.db import models
from datetime import datetime
class Job(models.Model):
    JOB_TYPES = [
        ('FT', 'Full-time'),
        ('PT', 'Part-time'),
        ('IN', 'Intern'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    job_type = models.CharField(max_length=2, choices=JOB_TYPES)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

def upload_resume(instance, filename):
        print(f"Uploading {filename} for {instance.name}")
        ext = filename.split('.')[-1]
        filename = f"{instance.name.replace(' ', '_').lower()}.{ext}"
        return os.path.join('resumes', filename)

class Applicant(models.Model):
    job = models.ForeignKey(Job, related_name='applicants', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    resume = models.FileField(upload_to=upload_resume)
    applied_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} applied for {self.job.title}"
    