from .models import Class_Master,Class_Member
from django import forms

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class_Master
        fields = ('class_name','course_id','Instructor_id','schedule_startdate',
                  'status','Class_completion_status','Extra_notes')

class Class_MemberForm(forms.ModelForm):
    class Meta:
        model = Class_Member
        fields = ('class_id','member_id')