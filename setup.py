#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='clarify_python_2',
    version='1.0.0',
    description='The Clarify Python 2 Helper Library wraps the entire Clarify API in Python 2.x function calls.',
    long_description=readme + '\n\n' + history,
    author='Paul Murphy',
    author_email='murphy@clarify.com',
    url='https://github.com/murphy/clarify_python_2',
    packages=[
        'clarify_python_2',
    ],
    package_dir={'clarify_python_2':
                 'clarify_python_2'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='clarify_python_2',
    classifiers=[
        'Development Status :: Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
)
