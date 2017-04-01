from .models import Schedule_Master,Schedule_Syllabus
from django import forms

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule_Master
        fields = ('Class_id','Schedule_datetime','Schedule_description','Schedule_title',
                  'Schedule_title','Class_held_status','Extra_notes','Status')

class ScheduleSyllabusForm(forms.ModelForm):
    class Meta:
        model = Schedule_Syllabus
        fields = ('Schedule_master_id','Session_type','Extra_notes')





