from django.conf import settings
from django.core import mail
from django.test import SimpleTestCase, override_settings

form_data = {
    'name': 'Daniel',
    'email': 'daniel@example.com',
    'subject': 'subject',
    'message': 'message',
}


@override_settings(
    CONTACT_URL='http://test-server.com/contact/',
    THANKS_URL='http://test-server.com/thanks/'
)
class ContactTestCase(SimpleTestCase):
    def test_send_email(self):
        self.client.post('/contact/', form_data)
        self.assertEqual(len(mail.outbox), 1)

    def test_email_subject(self):
        self.client.post('/contact/', form_data)
        self.assertEqual(mail.outbox[0].subject, 'Contact - subject')

    def test_valid_form_redirect(self):
        response = self.client.post('/contact/', form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.get('Location'), settings.THANKS_URL)
        pass

    def test_invalid_form_redirect(self):
        invalid_data = form_data.copy()
        invalid_data['name'] = ''
        response = self.client.post('/contact/', invalid_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.get('Location'), settings.CONTACT_URL)
