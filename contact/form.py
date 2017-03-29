from django import forms
from .models import Contact_Us

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_Us
        fields = ['name','email','follow_up','extra_note','subject']