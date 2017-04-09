from django.shortcuts import render, redirect
from .form import ScheduleForm, ScheduleSyllabusForm
from .models import Schedule_Master, Schedule_Syllabus
from django.http import HttpResponse
from login.models import UserProfile,User
from course.models import instructor_course,course_details

# Create your views here.

def Add_Schedule(request):
    if request.user.is_authenticated():
        if request.POST:
            form = ScheduleForm( request.POST )
            if form.is_valid():
                form.save()
                return redirect('/view_class/')
            else:
                form = ScheduleForm()
                return render(request,'add_schedule.html',{'form':form})
        else:
            form = ScheduleForm()
            return render(request,'add_schedule.html',{'form':form})


def Change_Schedule(request):
    if request.user.is_authenticated():
        user = request.user
        if request.POST:
            Schedule_master_id = request.POST.get('Schedule_master_id')
            schedule = Schedule_Master.objects.filter( Schedule_master_id = Schedule_master_id )
            return render(request, 'change_schedule.html', {'schedule': schedule})
        else:
            return redirect('/view_class/')

def Update_Schedule(request):
    if request.user.is_authenticated():
        user = request.user
        if request.method=="POST":
            Schedule_master_id = request.POST.get('Schedule_master_id')
            Schedule_description = request.POST.get('Schedule_description')
            Schedule_title = request.POST.get('Schedule_title')
            Class_held_status = request.POST.get('Class_held_status')
            Extra_notes = request.POST.get('Extra_notes')
            Status = request.POST.get('Status')
            Schedule_Master.objects.filter(Schedule_master_id = Schedule_master_id).update(Schedule_description = Schedule_description)
            Schedule_Master.objects.filter(Schedule_master_id = Schedule_master_id).update(Schedule_title = Schedule_title)
            Schedule_Master.objects.filter(Schedule_master_id = Schedule_master_id).update(Class_held_status = Class_held_status)
            Schedule_Master.objects.filter(Schedule_master_id = Schedule_master_id).update(Extra_notes = Extra_notes)
            Schedule_Master.objects.filter(Schedule_master_id = Schedule_master_id).update(Status = Status)
            return redirect('/view_class/')
        else:
            Schedule_master_id = request.POST.get('Schedule_master_id')
            schedule = Schedule_Master.objects.filter(Schedule_master_id=Schedule_master_id)
            return render(request, 'change_schedule.html', {'schedule': schedule})