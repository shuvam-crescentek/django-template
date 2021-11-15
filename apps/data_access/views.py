from django import forms
from django.contrib.auth.forms import AuthenticationForm as AuthForm
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.views import LoginView


class AuthenticationForm(AuthForm):

    username = UsernameField(
        widget=forms.TextInput(attrs={"class": "form-control", "autofocus": True})
    )

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "autocomplete": "current-password",
            }
        ),
    )


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
