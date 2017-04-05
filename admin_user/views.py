from django.shortcuts import render
from login.models import UserProfile
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponse
from course.models import course_details,member_course,instructor_course
from orders.models import Orders,Orders_Item
from class_details.models import Class_Master,Class_Member
from class_details.form import Class_MemberForm,ClassForm

# Create your views here.

def show_details(request):
    if request.user.is_authenticated():
        if request.POST:
            print "in Post "
            user_id = request.POST.get('user_id')
            print user_id
            data = User.objects.filter(id=user_id)
            data1 = UserProfile.objects.filter(user_id=data.values()[0]['id'])
            print data
            print data1
            return render(request, "show_details.html", {'data': data, 'data1': data1})
        else:
            return redirect('manage_instructor')
    else:
        return redirect('login')


def manage_user(request):
    if request.user.is_authenticated():
        data = UserProfile.objects.all().filter().values()
        return render(request, 'manage_user.html', {'data': data})
    else:
        return redirect('login')


def AdminProfile(request):
    if request.user.is_authenticated():
        MemberCourse = member_course.objects.all()
        InstructorCourse = instructor_course.objects.all()
        return render(request, 'admin.html',{'member':MemberCourse,'instructor':InstructorCourse})
    else:
        return redirect('login')


def manage_course(request):
    if request.user.is_authenticated():
        data = course_details.objects.all().values()
        return render(request, 'manage_course.html',{'data':data})
    else:
        return redirect('login')

def admin_changePassword(request):
    if request.user.is_authenticated():
        if request.POST:
            if request.user.check_password(request.POST['oldpass']):
                password = request.POST.get('password')
                cpassword = request.POST.get('cpassword')
                if password == cpassword:
                    user = request.user
                    user.set_password(password)
                    user.save()
                    return render(request,'login.html',{'display':"Password Changed"})
                else:
                    return render(request,'login.html',{'display':"Password Didnt Match"})
        else:
            return render(request, 'edit_profile.html')

def Payment_Details(request):
    if request.user.is_authenticated():
        data = UserProfile.objects.filter(usertype = "member")# (member id = 16, id = 3)
        id = data.values()[1]['user_id']
        member_id = " "
        instructor = " "
        order_item = Orders_Item.objects.filter( member_id = id )
        order = Orders.objects.filter( order_item_id = order_item)
        orderall = Orders.objects.all()
        for order_item_id in orderall:
            member_id = order_item_id.order_item_id.member_id
        classmember = Class_Member.objects.filter( member_id = member_id)
        try:
            for class_id in classmember:
                instructor =  class_id.class_id.Instructor_id
            context = {
                "order": order,
                "orderitem": order_item,
                "instructor": instructor,
                "data": data,
                "orderall": orderall,
            }
            return render(request, 'payment_details.html', context)
        except:
            context = {
                "order": order,
                "orderitem": order_item,
                "instructor": instructor,
                "data": data,
                "orderall": orderall,
            }
            return render(request, 'payment_details.html', context)


def Member_Class(request):
    if request.user.is_authenticated():
        form = Class_MemberForm( request.POST )
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('/admin_addinstructor/')
        else:
            form = Class_MemberForm()
            Class = " "
            class_member = " "
            class_data = Class_Master.objects.all()
            class_member = Class_Member.objects.all()

            return render(request,'admin_addinstructor.html',{'form':form,'class_data':class_data,'member':class_member})
