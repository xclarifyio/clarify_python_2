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
    name='op3nvoice_python_2',
    version='0.7.0',
    description='The OP3Nvoice Python 2 Helper Library wraps the entire OP3Nvoice API in Python 2.x function calls.',
    long_description=readme + '\n\n' + history,
    author='Paul Murphy',
    author_email='murphy@op3nvoice.com',
    url='https://github.com/murphy/op3nvoice_python_2',
    packages=[
        'op3nvoice_python_2',
    ],
    package_dir={'op3nvoice_python_2':
                 'op3nvoice_python_2'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='op3nvoice_python_2',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)