import requests
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class CaptchaField(forms.CharField):
    def validate(self, value):
        super().validate(value)

        url = "https://www.google.com/recaptcha/api/siteverify"
        data = {
            "secret": settings.RECAPTCHA_SECRET_KEY,
            "response": value,
        }
        response = requests.post(url, data)

        if not response.json().get("success", False):
            raise ValidationError(_("Invalid CAPTCHA"), code="captcha")


class ContactForm(forms.Form):
    name = forms.CharField(max_length=45)
    email = forms.EmailField(max_length=64)
    message = forms.CharField(max_length=1000)
    captcha_response = CaptchaField()
