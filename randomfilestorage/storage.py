# -*- coding: utf-8 -*-

import os
from django.utils.crypto import get_random_string
from django.core.files.storage import FileSystemStorage


class RandomFileSystemStorage(FileSystemStorage):

    def get_valid_name(self, name):
        file_root, file_ext = os.path.splitext(name)
        return "%s%s" % (get_random_string(32).lower(), file_ext)

    def get_available_name(self, name):
        dir_name, file_name = os.path.split(name)
        file_root, file_ext = os.path.splitext(file_name)
        while self.exists(name):
            name = os.path.join(dir_name, "%s%s" % (get_random_string(32).lower(), file_ext))
        return name
