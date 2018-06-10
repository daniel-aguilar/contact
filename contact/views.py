from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import ContactForm


@csrf_exempt
@require_POST
def contact(request):
    captcha_field = 'captcha_response'

    data = request.POST.copy()
    data[captcha_field] = request.POST.get('g-recaptcha-response')

    form = ContactForm(data)

    if form.is_valid():
        template = get_template('contact/message')

        send_mail(
            'New message from your contact form',
            template.render(form.cleaned_data),
            None,
            [settings.EMAIL_TO_ADDRESS]
        )
        return HttpResponseRedirect(settings.THANKS_URL)
    else:
        return HttpResponseRedirect(settings.ERROR_URL)
