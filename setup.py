#!/usr/bin/env python

from setuptools import setup, find_packages

# The text of the README file
with open( 'Readme.md' ) as f:
    README = f.read()

setup(
    name='complicated',
    version='1.0.0',
    description='Complicated python api. Control Apple Watch Complications with WebHooks',
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/frenchie4111/complicated-python",
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
