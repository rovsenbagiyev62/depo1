from django import forms
from django.contrib.auth.models import User
from myapp.models import UserProfIleinfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfIleinfo
        fields = ('portfolio_site','profile_pic')
