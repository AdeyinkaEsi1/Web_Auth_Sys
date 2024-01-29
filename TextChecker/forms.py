from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        labels = {
            "name": _("Writer"),
        }
        error_messages = {
            "name": {
                "max_length": _("This writer's name is too long."),
            },
        }


class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = "__all__"
        fields = ['email', 'pword']
       