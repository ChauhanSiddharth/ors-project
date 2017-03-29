from django import forms
from .models import course_details,material


class course_forms(forms.ModelForm):
    class Meta:
        model = course_details
        fields = ['title','image','description','status','duration','fees']

class material_forms(forms.ModelForm):
    class Meta:
        model = material
        fields =  ['course_id','mname','date','files']