from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    re_password = forms.CharField(label='Repeat password', widget=forms.PasswordInput())