Contact
=======

.. image:: https://travis-ci.com/daniel-aguilar/contact.svg?branch=master
   :target: https://travis-ci.com/daniel-aguilar/contact

.. image:: https://coveralls.io/repos/github/daniel-aguilar/contact/badge.svg?branch=master
   :target: https://coveralls.io/github/daniel-aguilar/contact?branch=master

Dead simple contact form back-end.

Requisites
----------

* Python 3.6+
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
* ``HOMEPAGE_URL``: Home page URL of your website.
* ``CONTACT_URL``: *Contact* URL page of your website (e.g.
  ``http://website.com/contact/``).

Run it::

    ./manage.py runserver

Testing
-------

Run the ``test`` target::

    make test

.. _`reCAPTCHA API key`: https://www.google.com/recaptcha/
.. _`AWS SES`: https://aws.amazon.com/ses/
