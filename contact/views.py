from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import ContactForm


@csrf_exempt
@require_POST
def contact(request):
    data = request.POST.copy()
    data.setlist('captcha_response', data.pop('g-recaptcha-response', None))

    form = ContactForm(data)

    if form.is_valid():
        template = get_template('contact/message', 'plaintext')

        send_mail(
            'New message from your contact form',
            template.render(form.cleaned_data),
            settings.EMAIL_ADDRESS,
            [settings.EMAIL_ADDRESS]
        )
        return render(
            request,
            'contact/success.html',
            {'back_url': settings.HOMEPAGE_URL}
        )
    else:
        return render(
            request,
            'contact/error.html',
            {'back_url': settings.CONTACT_URL}
        )
