# nlp_app/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .models import FieldData

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']



class FieldDataForm(forms.ModelForm):
    class Meta:
        model = FieldData
        fields = '__all__'

