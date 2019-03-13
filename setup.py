#!/usr/bin/env python

from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path( __file__ ).parent

# The text of the README file
README = ( HERE / "Readme.md" ).read_text()

setup(
    name='complicated',
    version='1.0.0',
    description='Complicated python api. Control Apple Watch Complications with WebHooks',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Mike Lyons',
    author_email='mdl0394@gmail.com',
    packages=find_packages( exclude=[ 'tmp' ] ),
    scripts=[
        'bin/complicated'
    ],
    install_requires=[
        'requests'
    ],
    license="MIT",
)
