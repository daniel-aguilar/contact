Interaction
===========

.. image:: https://travis-ci.com/daniel-aguilar/interaction.svg?branch=master
   :target: https://travis-ci.com/daniel-aguilar/interaction

.. image:: https://coveralls.io/repos/github/daniel-aguilar/interaction/badge.svg?branch=master
   :target: https://coveralls.io/github/daniel-aguilar/interaction?branch=master

Simple form back-end focused on communication.

Requisites
----------

* Python 3.6+
* Make
* A `reCAPTCHA API key`_
* A transactional email provider (e.g. `Amazon SES`_)
* A website

Building
--------

Install the dependencies::

    pip install -r requirements.txt

Create a ``.env`` file in the root directory, with the following variables:

* ``DJANGO_SETTINGS_MODULE``: The current Django settings you want to use (e.g.
  ``interaction.settings.dev``).
* ``EMAIL_HOST``
* ``EMAIL_HOST_USER``
* ``EMAIL_HOST_PASSWORD``
* ``EMAIL_SENDER``: Address from which email is sent.
* ``EMAIL_RECIPIENT``: Email address for *notifications* (e.g. contact form messages).
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
.. _`Amazon SES`: https://aws.amazon.com/ses/
