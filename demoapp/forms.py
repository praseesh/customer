from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer 
        fields = "__all__"
        # fields= ['firstname', 'address','phno']

# class CustomerForm(forms.Form):
#     first_name=forms.CharField(max_length=20)
#     last_name-forms.CharField(max_length=20)
#     password=forms.Charfield(widget=forms.PasswordInput())