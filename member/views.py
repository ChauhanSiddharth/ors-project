from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from login.models import UserProfile
from course.models import course_details, instructor_course
from login.forms import User_Form, Details_Form
# Create your views here.

def changePassword(request):
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
                    return render(request,'account.html',{'display':"Password Didnt Match Try Again"})
            else:
                return render(request, 'login.html', {'display': "Password error"})
        else:
            return render(request,'account.html')

def DeleteAccount(request):
    if request.user.is_authenticated():
        if request.POST:
            if request.user.check_password(request.POST['password']):
                user = request.user
                account = User.objects.get( id = user.id )
                account.delete()
                return render(request,'login.html',{'display':"User is Deleted"})
            else:
                return render(request, 'accountset.html',{'display':"Incorrect Password"})
        else:
            return render(request,'accountset.html')

#member instructor profile edit
def editProfile(request):
    if request.user.is_authenticated():
        user = request.user
        if request.POST:
            firstname = request.POST.get('firstname')
            middlename = request.POST.get('middlename')
            lastname = request.POST.get('lastname')
            address = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            contact = request.POST.get('contact')
            skills = request.POST.get('skills')
            qualification = request.POST.get('qualification')
            UserProfile.objects.filter(user = user.id).update(firstname = firstname)
            UserProfile.objects.filter(user = user.id).update(middlename = middlename)
            UserProfile.objects.filter(user = user.id).update(lastname = lastname)
            UserProfile.objects.filter(user = user.id).update(address = address)
            UserProfile.objects.filter(user = user.id).update(city = city)
            UserProfile.objects.filter(user = user.id).update(state = state)
            UserProfile.objects.filter(user = user.id).update(contact = contact)
            UserProfile.objects.filter(user = user.id).update(qualification = qualification)
            UserProfile.objects.filter(user = user.id).update(skills = skills)
            details = UserProfile.objects.filter(user=user)
            return render(request,'changeprofile.html',{'display':"Profile Updated",'details':details})
        else:
            user = request.user
            details = UserProfile.objects.filter(user = user)
            return render(request,'changeprofile.html',{'details':details})

def MemberProfile(request):
    if request.user.is_authenticated():
        user = request.user
        data = UserProfile.objects.filter(user = user)
        return render(request, 'profile.html', {'details': data})

def Dashboard(request):
    if request.user.is_authenticated():
        user = request.user
        data = UserProfile.objects.filter( user = user.id )
        skills = data.values()[0]['skills']
        coursedata = course_details.objects.filter(title=skills)
        return render(request,'home.html',{'data':data,'course':coursedata})

