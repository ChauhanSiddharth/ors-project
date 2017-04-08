from django.shortcuts import render, redirect
from login.models import UserProfile
from course.models import course_details,material,instructor_course,member_course
from .forms import material_form
import datetime
# Create your views here.
def instructor_courses(request):
    if request.user.is_authenticated():
        user = request.user
        data1 = UserProfile.objects.filter( user_id = user.id )
        print data1
        skills = data1.values()[0]['skills']
        print skills
        course = instructor_course.objects.filter( instructor_id = user.id )
        print course
        try:
            course_id = course.values()[0]['id']
            print course_id
            data1 = material.objects.filter(course_id_id = course_id)
            print data1
        except Exception:
            return render(request,'instructor_course.html',{'course':course,'material':data1})
        return render(request,'instructor_course.html',{'course':course,'material':data1})



def add_material(request):
    if request.user.is_authenticated():
        user = request.user
        form = material_form(request.POST, request.FILES or None)
        icourse = instructor_course.objects.filter( instructor_id = user.id )
        courseid = icourse.values()[0]['id']
        print courseid
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('instructor_course')
        return render(request,'add_material.html',{'form':form,'course_id':courseid})

def delete_material(request):
    user = request.user
    if request.POST:
        id = request.POST.get('id')
        materials = material.objects.filter( id = id )
        materials.delete()
        return redirect('/view_class/')