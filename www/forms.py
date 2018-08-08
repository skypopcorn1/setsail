from accounts.models import Role
from race.models import Race

from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class LoginForm(forms.Form):
    email       = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'loginField'}))
    password    = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'loginField'}))

    class Meta:
        model = User
        fields = ['email', 'password']

class RaceForm(forms.ModelForm):
    race_course     = forms.CharField(label='Race Course', widget=forms.TextInput(attrs={'class' : 'time-field'}))
    race_start      = forms.DateTimeField(label='Race Start', widget=forms.DateTimeInput(attrs={'class' : 'time-field'}))
    race_finish     = forms.DateTimeField(label='Race Finish', widget=forms.DateTimeInput(attrs={'class' : 'time-field'}))
    class Meta:
        model = Race
        fields = ['race_course', 'race_start', 'race_finish']

class RegistrationForm(forms.ModelForm):
    email       = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'loginField'}))
    password    = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'loginField'}))
    password2   = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class' : 'loginField'}))
    user_role   = forms.ModelChoiceField(queryset=Role.objects.all(),label='Primary role', widget=forms.Select())
    class Meta:
        model = User
        fields = ['email', 'password','user_role']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already registered")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
