from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import ContactForm


@csrf_exempt
@require_POST
def send_message(request):
    data = request.POST.copy()
    data.setlist('captcha_response', data.pop('g-recaptcha-response', []))

    form = ContactForm(data)

    if form.is_valid():
        template = get_template('message', 'plaintext')

        send_mail(
            'New message from your contact form',
            template.render(form.cleaned_data),
            settings.EMAIL_SENDER,
            [settings.EMAIL_RECIPIENT]
        )
        return render(request, 'success.html')
    return render(request, 'error.html')
