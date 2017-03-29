from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import instructor_courses,add_material,add_schedule
urlpatterns = [
url(r'^instructor_course/', instructor_courses, name="instructor_course"),
url(r'^add_material/', add_material ,name ='add_material' ),
url(r'^add_schedule/', add_schedule ,name ='add_schedule' ),
# s
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)