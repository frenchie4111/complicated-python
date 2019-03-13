#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='complicated',
    version='1.0',
    description='Complicated python api. Control Apple Watch Complications with WebHooks',
    author='Mike Lyons',
    author_email='mdl0394@gmail.com',
    packages=find_packages( exclude=[ 'tmp' ] ),
    scripts=[
        'bin/complicated'
    ],
    install_requires=[
        'requests'
    ]
)
