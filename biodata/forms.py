from django import forms
from .models import Employee



# Creating a model to handle our forms
class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        # Creating our form fields with Django's in-built forms
        fields = (
            'firstname',
            'lastname',
            'age',
            'gender',
            'address',
            'date_of_birth',
            'email'
            )
            