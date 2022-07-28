from django.contrib.auth.forms import AuthenticationForm
from django import forms

from contacts.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone', 'job', 'education')

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'u-border-3 u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'u-border-3 u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle',

            }),
            'phone': forms.TextInput(attrs={
                'class': 'u-border-3 u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle',
                'placeholder': 'شماره تماس به همراه کد',

            }),
            'job': forms.TextInput(attrs={
                'class': 'u-border-3 u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle',
            }),
            'education': forms.TextInput(attrs={
                'class': 'u-border-3 u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle'
            })
        }


class ContactForm2(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone', 'job', 'education')

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'شماره تماس به همراه کد',

            }),
            'job': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'education': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = ' form-control'
        self.fields['password'].widget.attrs['class'] = ' form-control'
