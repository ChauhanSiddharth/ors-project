from django import forms
from course.models import material

class material_form(forms.ModelForm):
    class Meta:
        model = material
        fields = ['course_id','mname','files']