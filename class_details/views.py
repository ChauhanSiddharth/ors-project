from django.shortcuts import render, redirect
from .models import Class_Member,Class_Master
from .form import Class_MemberForm,ClassForm
from course.models import material
from course.models import course_details,instructor_course

# Create your views here.

def View_Class(request):
    if request.user.is_authenticated():
        user = request.user
        instructor = instructor_course.objects.filter( instructor_id = user.id )
        class_details = Class_Master.objects.filter( Instructor_id = instructor )
        classno = class_details.values()[0]['class_id']
        class_member = Class_Member.objects.filter( class_member_id = classno )
        course = instructor_course.objects.filter(instructor_id=user.id)
        try:
            course_id = course.values()[0]['id']
            materials = material.objects.filter(course_id_id=course_id)
        except Exception:
            return render(request,'class_details.html',{'data':class_details,'member':class_member})
        return render(request, 'class_details.html', {'data': class_details, 'member': class_member,'material':materials})

def Add_Class(request):
    if request.user.is_authenticated():
        form = ClassForm( request.POST )
        if request.POST:
            if form.is_valid():
                form.save()
                return  redirect('/view_class/')
        else:
            form = ClassForm()
            user = request.user
            instructor = instructor_course.objects.filter( instructor_id = user.id )
            courseid = instructor.values()[0]['course_id_id']
            coursedata = course_details.objects.filter( id = courseid )
            print coursedata
            return render(request,'add_class.html',{'form':form,'course':coursedata,'instructor':instructor})
