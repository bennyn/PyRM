#!/usr/bin/env python
# coding: utf-8

"""
    PyRM distutils setup
    ~~~~~~~~~~~~~~~~~~~~~~~

    :copyleft: 2009-2010 by the PyRM team, see AUTHORS for more details.
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

import os

from setuptools import setup, find_packages

from pyrm import VERSION_STRING


PACKAGE_ROOT = os.path.dirname(os.path.abspath(__file__))


def get_authors():
    try:
        f = file(os.path.join(PACKAGE_ROOT, "AUTHORS"), "r")
        authors = [l.strip(" *\r\n") for l in f if l.strip().startswith("*")]
        f.close()
    except Exception, err:
        authors = "[Error: %s]" % err
    return authors


def get_long_description():
    try:
        f = file(os.path.join(PACKAGE_ROOT, "README"), "r")
        long_description = f.read().strip()
        f.close()
    except Exception, err:
        long_description = "[Error: %s]" % err
    return long_description



setup(
    name='PyRM',
    version=VERSION_STRING,
    description='PyRM is an open-source "Rechnungs-Manager" using django.',
    long_description=get_long_description(),
    author=get_authors(),
    maintainer="Jens Diemer",
    url='http://www.PyRM.org',
    packages=find_packages(
        exclude=[".project", ".pydevproject", ]
    ),
    include_package_data=True, # include package data under svn source control
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Development Status :: 2 - Pre-Alpha',
#        'Development Status :: 3 - Alpha',
#        "Development Status :: 4 - Beta",
#        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
#        "Intended Audience :: Education",
#        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        'Framework :: Django',
        "Topic :: Database :: Front-Ends",
        "Topic :: Documentation",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Operating System :: OS Independent",
    ]
)
