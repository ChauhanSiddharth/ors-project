from django.contrib import admin

from .models import Schedule_Master
from .models import Schedule_Syllabus

# Register your models here.
admin.site.register(Schedule_Master)
admin.site.register(Schedule_Syllabus)