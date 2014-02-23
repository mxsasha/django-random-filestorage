#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import randomfilestorage

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = randomfilestorage.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-random-filestorage',
    version=version,
    description="""Django storage class that assigns random filenames to all stored files.""",
    long_description=readme + '\n\n' + history,
    author='Erik Romijn',
    author_email='eromijn@solidlinks.nl',
    url='https://github.com/erikr/django-random-filestorage',
    packages=[
        'randomfilestorage',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-random-filestorage',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
