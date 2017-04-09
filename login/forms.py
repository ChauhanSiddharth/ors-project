from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class User_Form(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput)
    email = forms.EmailField( widget=forms.EmailInput )
    class Meta:
        model = User
        username = forms.EmailField(max_length=64,
                                    help_text="The person's email address.")
        fields = ['username','email','password']


class Details_Form(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['user', 'firstname', 'middlename', 'lastname', 'gender', 'usertype', 'address', 'city', 'state',
                  'contact', 'qualification','skills','profile_pic', 'resume', 'joiningdate']

    def save(self, commit=True, fail_silently=False):
        super(Details_Form, self).save(commit)
