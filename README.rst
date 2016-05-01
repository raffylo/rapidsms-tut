
RapidSMS is a free and open source framework for building interactive SMS applications, which integrates tightly with Django to provide a rich reporting interface. It was created by the Innovation Team at UNICEF, and is under development by the RapidSMS Team.

I am not involved in any way in the above; please check out https://github.com/rapidsms/rapidsms for the original work.

Rapidsms_Tut_Vote
========================

Below you will find basic setup instructions for the ``rapidsms_tut_vote``
project. To begin you should have the following applications installed on your
local development system:

- `Python >= 2.7 (including Python 3) <http://www.python.org/getit/>`_
- `pip >= 7.0.3 <http://www.pip-installer.org/>`_
- `virtualenv >= 13.0.3 <http://www.virtualenv.org/>`_

Getting Started
---------------

To setup your local environment you should create a virtualenv and install the
necessary requirements::

    virtualenv rapidsms_tut_vote-env

On Posix systems you can activate your environment like this::

    source rapidsms_tut_vote-env/bin/activate

On Windows, you'd use::

    rapidsms_tut_vote-env\Scripts\activate

Then::

    cd rapidsms_tut_vote
    pip install -U -r requirements/base.txt

Run migrate::

    python manage.py migrate

You should now be able to run the development server::

    python manage.py runserver
