import requests
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class CaptchaField(forms.CharField):
    def validate(self, value):
        super().validate(value)

        url = (
            f"https://recaptchaenterprise.googleapis.com/v1/projects/delicious-gyros/"
            f"assessments?key={settings.RECAPTCHA_API_KEY}"
        )
        data = {
            "event": {
                "token": value,
                "siteKey": settings.RECAPTCHA_SITE_KEY,
            },
        }
        response = requests.post(url, json=data)
        response.raise_for_status()

        token_props = response.json().get("tokenProperties", {})
        valid = token_props.get("valid", False)

        if not valid:
            raise ValidationError(_("Invalid CAPTCHA"), code="captcha")


class ContactForm(forms.Form):
    name = forms.CharField(max_length=45)
    email = forms.EmailField(max_length=64)
    message = forms.CharField(max_length=1000)
    captcha_response = CaptchaField()
