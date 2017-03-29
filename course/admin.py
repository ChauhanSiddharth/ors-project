from django.contrib import admin
from .models import course_details,member_course,instructor_course,material
# Register your models here.
admin.site.register(course_details)
admin.site.register(instructor_course)
admin.site.register(member_course)
admin.site.register(material)