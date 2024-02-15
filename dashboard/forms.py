from django import forms
from . models import *

class NotesForm(forms.ModelForm):
    class Meta:
        model =Notes
        fields = ['title','description']

class DateInput(forms.DateInput):
    input_type='date'        
        

class HomeworksForm(forms.ModelForm):
    class Meta:
        model =Homeworks
        widgets = {'due': DateInput()}
        fields = ['subject','title','description','due','is_finished']