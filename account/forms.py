from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(min_length=8, required=True,
                               widget=forms.PasswordInput)
    password_confirmation = forms.CharField(min_length=8, required=True,
                               widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation',
                  'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Such email is already registered by another person')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists(): #username2 - value!
            raise forms.ValidationError('Such username is already registered by another person')
        return username

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        confirm_password = data.pop('password_confirmation')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        return data

    def save(self, commit=True):

        from .utils import send_welcome_email

        user = User.objects.create_user(**self.cleaned_data)
        send_welcome_email(user.email)
        return user

