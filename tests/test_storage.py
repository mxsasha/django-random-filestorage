#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-random-filestorage
------------

Tests for `django-random-filestorage` models module.
"""
import tempfile
import os
import unittest

from randomfilestorage.storage import RandomFileSystemStorage


class TestRandomfilestorage(unittest.TestCase):

    def setUp(self):
        self.temp_storage_location = tempfile.mkdtemp()
        self.storage = RandomFileSystemStorage(location=self.temp_storage_location)

    def test_get_valid_name(self):
        name1 = self.storage.get_valid_name('foobar')
        name2 = self.storage.get_valid_name('foobar.txt')
        self.assertNotEqual(name1, name2)
        self.assertFalse('foobar' in name1 or 'foobar' in name2)

    def test_get_available_name(self):
        file_path = os.path.join(self.temp_storage_location, 'foobar.txt')
        open(file_path, 'a').close()
        available_path = self.storage.get_available_name(file_path)
        self.assertNotEqual(available_path, file_path)
        self.assertFalse('foobar' in available_path)
