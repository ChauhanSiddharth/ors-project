from django.shortcuts import render
from django.shortcuts import render
from login.models import UserProfile
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponse
from course.forms import course_forms,material_forms
from .models import course_details, member_course



# Create your views her


def add_course(request):
    if request.user.is_authenticated():
        if request.POST:
            print "in post"
            form = course_forms(request.POST, request.FILES or None)
            if form.is_valid():
                print "before save"
                form.save()
                print "after save"
                return redirect('manage_course')
            else:
                print "no"
                return render(request, 'add_course.html')
        context = {
            'form': course_forms
        }
        return render(request, 'add_course.html',context)
    else:
        return redirect('login')

def show_course(request):
    if request.user.is_authenticated():
        if request.POST:
            id = request.POST.get('id')
            data = course_details.objects.filter(id = id)
            print data
            return render(request,'show_course.html',{'data':data})
    else:
        return redirect('login')

def delete_course(request):
    if request.user.is_authenticated():
        if request.POST:
            id = request.POST.get('id')
            data = course_details.objects.filter(id = id).delete()
            return redirect('manage_course')
    else:
        return redirect('login')


def courses(request):
    if request.user.is_authenticated():
        user = request.user
        print user
        data = course_details.objects.all()
        mycourse = member_course.objects.filter( member_id = user.id )
        print mycourse
        if user.userprofile.usertype == 'member':
            return render(request,'courses.html',{'data':data,'mycourse':mycourse})
        else:
            return redirect('instructor_course')
    else:
        return redirect('login')

def view_course(request):
    if request.user.is_authenticated():
        if request.POST:
            id = request.POST.get('id')
            data = course_details.objects.filter(id = id)
            return render(request,'view_course.html',{'data':data})
        else:
            return redirect('courses')
    else:
        return redirect('login')

def searchbox(request):
    if request.user.is_authenticated():
        user = request.user
        if request.GET:
            search_query = request.GET.get('search_box', None)
            print search_query
            try:
                course = course_details.objects.filter( title = search_query )
                data = course_details.objects.all()
                mycourse = member_course.objects.filter(member_id=user.id)
                return render(request,'courses.html',{'course':course,'data':data,'mycourse':mycourse})
            except Exception:
                return Exception
        else:
            return render(request, 'courses.html')
