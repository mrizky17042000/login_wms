from django import forms
from .models import User


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'password',
        ]
