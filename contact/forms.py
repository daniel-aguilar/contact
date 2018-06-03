from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=45)
    email = forms.CharField(max_length=25)
    subject = forms.CharField(max_length=65)
    message = forms.CharField()
