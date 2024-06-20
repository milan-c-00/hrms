from django import forms
from .models import Client, Employee

class ClientForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    professional_email = forms.CharField(label='Professional Email')
    notes = forms.CharField(label='Notes',required=False)
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), label='Employee')
    image = forms.ImageField(label='Image',required=False) 
    
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'professional_email', 'notes', 'employee','image']
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        professional_email = cleaned_data.get("professional_email")
        employee = cleaned_data.get("employee")
        image = cleaned_data.get("image")

        if not first_name:
            self.add_error('first_name', 'This field is required.')
        if not last_name:
            self.add_error('last_name', 'This field is required.')
        if not professional_email:
            self.add_error('professional_email', 'This field is required.')
        if not employee:
            self.add_error('employee', 'This field is required.')


        return cleaned_data