from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import User_Form,Details_Form
from .models import UserProfile
from course.models import course_details
from member.views import Dashboard
from django.core import serializers
# Create your views here.

def login_views(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username = username, password=password)
        print user
        if user is not None:
            auth.login(request,user)
            data = UserProfile.objects.filter(user = user.id)
            if user.userprofile.usertype == 'administrator':
                return render(request,"admin.html")
            elif user.userprofile.usertype == 'member':
                return redirect(Dashboard)
                #return render(request,'home.html',{'details':data})
            elif user.userprofile.usertype == 'instructor':
                #return render(request, 'home.html', {'data': data,'course':coursedata})
                return redirect(Dashboard)
        else:
            return render(request,"login.html")
    return render(request,"login.html")

def logout_views(request):
    logout(request)
    return redirect(login_views)

def register_views(request):
    form = User_Form(request.POST or None)
    if request.POST:
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(details_views)
    context = {
        "form":form
    }
    return render(request, "register.html", context)

def details_views(request):
    if request.user.is_authenticated():
        user = request.user.id
        if request.POST:
            request.POST['user'] = user
            print request.POST
            user_form = Details_Form(request.POST,request.FILES)
            if user_form.is_valid():
                user_form.save()
                return redirect(login_views)
        user_form  = Details_Form(initial={"user":user})
        context = {
            "form": user_form,
            "user": user
        }
        return render(request, "forms.html", context)

#admin profile edit
def edit_profile(request):
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
            UserProfile.objects.filter(user=user.id).update(firstname=firstname)
            UserProfile.objects.filter(user=user.id).update(middlename=middlename)
            UserProfile.objects.filter(user=user.id).update(lastname=lastname)
            UserProfile.objects.filter(user=user.id).update(address=address)
            UserProfile.objects.filter(user=user.id).update(city=city)
            UserProfile.objects.filter(user=user.id).update(state=state)
            UserProfile.objects.filter(user=user.id).update(contact=contact)
            UserProfile.objects.filter(user=user.id).update(qualification=qualification)
            UserProfile.objects.filter(user=user.id).update(skills=skills)
            details = UserProfile.objects.filter(user=user)
            return render(request, 'edit_profile.html', {'display': "Profile Updated", 'details': details})
        else:
            user = request.user
            details = UserProfile.objects.filter(user=user)
            return render(request, 'edit_profile.html', {'details': details})

def delete_data(request):
    if request.user.is_authenticated():
        if request.POST:
            print "in Post "
            user_id = request.POST.get('user_id')
            print user_id
            query = User.objects.filter(id = user_id)
            print query
            query.delete()
            return redirect('manage_user')
        else:
            return redirect('manage_user')
    else:
        return redirect('login')
