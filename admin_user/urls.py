from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from course.views import add_course,show_course,delete_course
from course.views import courses,view_course
from member.views import Dashboard
from .views import (
show_details,
manage_user,
manage_course,
admin_changePassword
)



urlpatterns = [
url(r'^manage_user/', manage_user, name="manage_user"),
url(r'^show_details/', show_details,name="show_details"),
url(r'^manage_course/', manage_course, name="manage_course"),
url(r'^add_course/', add_course, name="add_course"),
url(r'^show_course/', show_course, name="show_course"),
url(r'^delete_course/', delete_course, name="delete_course"),
url(r'^usercourses/', courses , name="courses"),
url(r'^view_course/',view_course, name="view_course"),
url(r'^dashboard/',Dashboard, name="Dashboard"),
url(r'^changepassword/', admin_changePassword, name="AdminPassword")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)