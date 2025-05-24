from unittest.mock import MagicMock, patch

from django.core import mail
from django.core.exceptions import ValidationError
from django.test import SimpleTestCase, override_settings

from .forms import CaptchaField


@override_settings(
    EMAIL_SENDER="contact@website.com",
    EMAIL_RECIPIENT="daniel@website.com",
)
class ContactTestCase(SimpleTestCase):
    def setUp(self):
        self.form_data = {
            "name": "Alice",
            "email": "alice@example.com",
            "message": "message",
            "g-recaptcha-response": "I am not a robot",
        }

    @patch("messages.forms.CaptchaField.validate")
    def test_send_email(self, validate):
        self.client.post("/contact/", self.form_data)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].from_email, "contact@website.com")
        self.assertCountEqual(mail.outbox[0].recipients(), ["daniel@website.com"])

    @patch("messages.forms.CaptchaField.validate")
    def test_valid_form(self, validate):
        response = self.client.post("/contact/", self.form_data)

        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(
            [t.name for t in response.templates],
            ["message", "base.html", "success.html"],
        )

    @patch("messages.forms.CaptchaField.validate")
    def test_invalid_form(self, validate):
        validate.side_effect = ValidationError("Invalid CAPTCHA", code="captcha")
        response = self.client.post("/contact/", self.form_data)

        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(
            [t.name for t in response.templates], ["base.html", "error.html"]
        )


@patch("requests.post")
@patch("requests.Response")
class ContactFormTestCase(SimpleTestCase):
    def test_valid_captcha(self, post, Response):
        res = Response()
        res.json = MagicMock(return_value={"success": True})
        post.return_value = res

        field = CaptchaField()
        self.assertEqual(field.clean("I am not a robot"), "I am not a robot")

    def test_invalid_captcha(self, post, Response):
        res = Response()
        res.json = MagicMock(return_value={"success": False})
        post.return_value = res

        field = CaptchaField()
        with self.assertRaises(ValidationError) as cm:
            field.clean("I am a robot")

        self.assertEqual(cm.exception.code, "captcha")
