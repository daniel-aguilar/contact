from django.urls import path

from messages.views import send_message

urlpatterns = [
    path('contact/', send_message),
]
