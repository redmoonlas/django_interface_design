from django import forms
from django.utils.translation import ugettext as _



class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()


class ContactForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea)


class RegistrationForm(forms.Form):
        required_css_class = 'required'
        # error_css_class = 'error'

        username = forms.RegexField(
            regex=r'^[\w.@+-]+$',
            max_length=30,
            label=_("Username"),
            error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")}
        )
        email = forms.EmailField(label=_("E-mail"))
        password1 = forms.CharField(
            widget=forms.PasswordInput,
            label=_("Password")
        )
        password2 = forms.CharField(
            widget=forms.PasswordInput,
            label=_("Password (again)")
        )
        first_name = forms.RegexField(
            required=False,
            regex=r'^[\w.@+-]+$',
            max_length=30,
            label=_("first name"),
            error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")}
        )
        last_name = forms.RegexField(
            required=False,
            regex=r'^[\w.@+-]+$',
            max_length=30,
            label=_("last name"),
            error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")}
        )