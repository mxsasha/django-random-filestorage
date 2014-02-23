========
Usage
========

To use django-random-filestorage, you'll have to configure it as the storage backend.

This can be done for all relevant fields that do not have an explicit storage set up, with the ``DEFAULT_FILE_STORAGE``
setting in Django::

    DEFAULT_FILE_STORAGE="randomfilestorage.storage.RandomFileSystemStorage"

Or, you can set it on a specific field::

    from randomfilestorage.storage import RandomFileSystemStorage

    random_storage = RandomFileSystemStorage(location='/media/my_files')
    class Example(models.Model):
        my_file = FileField(storage=random_storage)

