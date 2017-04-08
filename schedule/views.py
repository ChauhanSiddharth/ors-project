from django.shortcuts import render, redirect
from .form import ScheduleForm, ScheduleSyllabusForm
from .models import Schedule_Master, Schedule_Syllabus
from django.http import HttpResponse

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
