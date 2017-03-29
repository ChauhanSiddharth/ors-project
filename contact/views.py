from django.shortcuts import render
from .models import Contact_Us
from .form import ContactForm

# Create your views here.

def Contact_View(request):
    if request.user.is_authenticated():
        form = ContactForm(request.POST, request.FILES or None)
        if request.POST:
            if form.is_valid():
                form.save()
                return render(request,'contact.html',{'form':form,'display':"Feedback Sent"})
        else:
            return render(request, 'contact.html',{'form':form})
