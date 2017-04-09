from django.shortcuts import render, redirect
from .models import Class_Member,Class_Master
from .form import Class_MemberForm,ClassForm
from course.models import material
from course.models import course_details,instructor_course
from schedule.models import Schedule_Master,Schedule_Syllabus

# Create your views here.

def View_Class(request):
    if request.user.is_authenticated():
        user = request.user
        instructor = instructor_course.objects.filter( instructor_id = user.id )
        try:
            class_details = Class_Master.objects.filter( Instructor_id = instructor )
            classno = class_details.values()[0]['class_id']
            class_member = Class_Member.objects.filter( class_id = classno )
            course = instructor_course.objects.filter(instructor_id=user.id)
            course_id = course.values()[0]['id']
            materials = material.objects.filter(course_id_id=course_id)
            schedule = Schedule_Master.objects.order_by('Schedule_datetime').filter( Class_id = classno )
        except Exception:
            return render(request,'class_details.html')
        context = {
            'data': class_details,
            'member': class_member,
            'material': materials,
            'schedule': schedule,
        }
        return render(request, 'class_details.html', context)

def Add_Class(request):
    if request.user.is_authenticated():
        form = ClassForm( request.POST )
        if request.POST:
            if form.is_valid():
                form.save()
                return  redirect('/view_class/')
        user = request.user
        instructor = instructor_course.objects.filter( instructor_id = user.id )
        instructorid = instructor.values()[0]['instructor_id_id']
        courseid = instructor.values()[0]['course_id_id']
        coursedata = course_details.objects.filter( id = courseid )
        print instructorid
        print courseid
        return render(request,'add_class.html',{'form':form,'course':courseid,'instructor':instructorid})
