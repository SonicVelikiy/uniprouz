from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required': '',
            'name': 'name',
            'id': 'name',
            'type': 'text',
            'class': 'form-input',
            'placeholder': 'Your Name',
            'minlength': '3'
        })
        self.fields["email"].widget.attrs.update({
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'class': 'form-input',
            'placeholder': 'Your Email',
        })
        self.fields["password1"].widget.attrs.update({
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'class': 'form-input',
            'placeholder': 'New password',
        })
        self.fields["password2"].widget.attrs.update({
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'class': 'form-input',
            'placeholder': 'Confirm password',
        })

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
