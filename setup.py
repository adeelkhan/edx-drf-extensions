#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import edx_rest_framework_extensions

setup(
    name='edx-drf-extensions-with-ratelimit',
    version=edx_rest_framework_extensions.__version__,
    description='edX extensions of Django REST Framework',
    author='edX',
    author_email='oscm@edx.org',
    url='https://github.com/adeelkhan/edx-drf-extensions.git',
    license='AGPL',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=1.8.9,<2.0',
        'djangorestframework==3.6.3',
        'djangorestframework-jwt>=1.7.2,<2.0.0',
        'python-dateutil>=2.0',
        'requests>=2.7.0,<3.0.0',
        'six==1.11.0',
        'django-ipware==1.1.0',
        'django-config-models==0.1.8',
        'django-ratelimit==1.1.0'
    ],
    dependency_links=[
        'git+https://github.com/edx/django-rest-framework.git@1ceda7c086fddffd1c440cc86856441bbf0bd9cb#egg=djangorestframework==3.6.3'
    ]
)
