=============================
django-random-filestorage
=============================

.. image:: https://badge.fury.io/py/django-random-filestorage.png
    :target: https://badge.fury.io/py/django-random-filestorage

.. image:: https://travis-ci.org/erikr/django-random-filestorage.png?branch=master
    :target: https://travis-ci.org/erikr/django-random-filestorage

.. image:: https://coveralls.io/repos/erikr/django-random-filestorage/badge.png?branch=master
    :target: https://coveralls.io/r/erikr/django-random-filestorage?branch=master

Django-random-filestorage is a Django storage class that assigns random filenames to all stored files.

If a user uploads a file named `foo.txt`, it
will be stored as `<60 random characters>.txt`. In cases where you refer users to uploaded files or images directly,
this will prevent them from finding other files, which they may not be authorised to see, by guessing the original
names used by your users.

Documentation
-------------

The full documentation is at https://django-random-filestorage.readthedocs.org.

Quickstart
----------

Install django-random-filestorage::

    pip install django-random-filestorage

Then use it in your entire Django project::

    DEFAULT_FILE_STORAGE="randomfilestorage.storage.RandomFileSystemStorage"

Or, set it on a specific field::

    from randomfilestorage.storage import RandomFileSystemStorage

    random_storage = RandomFileSystemStorage(location='/media/my_files')
    class Example(models.Model):
        my_file = FileField(storage=random_storage)


Why would you want to do this?
------------------------------

Let's say you have an app that manages all ice cream recipes you sell in your shop. Some of your recipes contain secret
ingredients, and are therefore only available to a small set of trusted users. We'll look at two icecreams: strawberry,
which has a fairly standard and non-secret recipe, and jellyfish, which is very secret.

The recipes are stored in PDFs, which are uploaded into a Django app that uses a FileField. As Django suggests,
the media directory is directly accessible through nginx or some other simple web server. So a user which is authorised
to see the strawberry recipe, will be sent to a PDF like ``http://example.com/media/recipes/strawberry.pdf``. They
will not see jellyfish in their list of recipes, as it's too secret.

However, given that the user knows that you sell jellyfish too, they can simply find that recipe on
``http://example.com/media/recipes/jellyfish.pdf``! There are many cases where names of documents, with differing access
levels, are in some way predictable. Dates are another predictable example. And filenames in FileFields are derived
from the original filename the user chose.

By making these filenames random, the person who can access
``http://example.com/media/recipes/ZXcAoL4wmhisYlBvHLoyt3fwfMXsMiVvgQTQOb40zOQIdag7KbEU5sy9b6GW.pdf``
will not be able to guess that the jellyfish recipe is available on
``http://example.com/media/recipes/qPRCEVAJd1RQvkd9OTTeY4hruW0Jvy5Qq0YIVtWPrwGWMgmUogYO8aPVRCxC.pdf``.

What issues are not resolved?
-----------------------------
Once a user knows the random string that was used to name the file, they could provide the link to others. Then again,
they could just as well download the file and provide it to others in some other way.

If you would like stricter control over who accesses certain files, you'll have to prevent direct access to (part of)
the media directory. You can serve those files through a Django view instead, but this comes at an additional
performance cost. A more performant but more complex alternative is to use Apache sendfile_ or nginx X-accel_.

.. _sendfile: https://tn123.org/mod_xsendfile/
.. _X-accel: http://wiki.nginx.org/X-accel
