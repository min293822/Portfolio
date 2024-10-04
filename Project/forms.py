from django import forms
from django.contrib.auth.models import User
from .models import UserDetails

class UserSignUpForm(forms.ModelForm):
    user_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name', 'id':'name'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'id':'password'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'id':'email'})
    )
    birth_date = forms.DateField(
        widget=forms.SelectDateWidget(attrs={'class': 'form-control', 'id':'birth'},years=range(1950, 2025))
    )
    sex = forms.ChoiceField(
        choices=[
            ('', 'Select Gender'),
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
            ('N', 'Prefer not to say'),
        ],
        widget=forms.Select(attrs={'class': 'form-control', 'id':'sex'})
    )


    class Meta:
        model = UserDetails
        fields = ['user_name', 'email', 'sex', 'birth_date', 'password']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['user_name'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        userinfo = super().save(commit=False)
        userinfo.user = user
        if commit:
            userinfo.save()
        return userinfo