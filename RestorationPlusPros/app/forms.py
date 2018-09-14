"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, max_length=120)
    contact_email = forms.EmailField(required=True, max_length=120)
    contact_phone = forms.CharField(required=False, max_length=120)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'rows':4})
    )
