from django.contrib import admin
from .models import JobsJob,JobsResume,Candidate

# Register your models here.

admin.site.register(JobsJob)
admin.site.register(JobsResume)
admin.site.register(Candidate)