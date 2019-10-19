from django import forms
from .models import Biodata



# Creating a model to handle our forms
class BiodataForm(forms.ModelForm):

    class Meta:
        model = Biodata
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
            