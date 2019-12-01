from django import forms
from .models import Employee,Position,kaam


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('ename','email','econtact')
        labels ={
            'fullname':'full name',
            'emp_code':'EMP. code'
        }


    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "select"

class kaamForm(forms.ModelForm):

    class Meta:
        model =kaam
        fields = ('ename','email','econtact','position')



