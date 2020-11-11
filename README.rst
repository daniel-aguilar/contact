Contact
=======

.. image:: https://github.com/daniel-aguilar/contact/workflows/build/badge.svg
   :target: https://github.com/daniel-aguilar/contact/actions

Dead simple contact form back-end.

Requisites
----------

* Python 3.9
* Make
* A `reCAPTCHA API key`_
* A transactional email provider (e.g. `AWS SES`_)
* A website

Building
--------

Install the dependencies::

    pip install -r requirements.txt

Create a ``.env`` file in the root directory, with the following variables:

* ``DJANGO_SETTINGS_MODULE``: The current Django settings you want to use (e.g.
  ``settings.dev``).
* ``EMAIL_HOST``
* ``EMAIL_HOST_USER``
* ``EMAIL_HOST_PASSWORD``
* ``EMAIL_SENDER``: Address from which email is sent.
* ``EMAIL_RECIPIENT``: Email address for *notifications* (i.e. contact form
  messages).
* ``RECAPTCHA_SECRET_KEY``

Run it::

    ./manage.py runserver

Testing
-------

Run the ``test`` target::

    make test

.. _`reCAPTCHA API key`: https://www.google.com/recaptcha/
.. _`AWS SES`: https://aws.amazon.com/ses/
