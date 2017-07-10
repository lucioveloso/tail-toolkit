#!/usr/bin/env python
import codecs
import os.path
import re

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


requires = ['boto3>=1.4.4',
            'botocore>=1.5.78']

setup_options = dict(
    name='tail-toolkit',
    version=find_version("tail_toolkit", "__init__.py"),
    description='An AWS tail command line interface (CLI). It helps you in tail some resoruces inside aws.',
    long_description=open('README.md').read(),
    author='Lucio Veloso Guimaraes',
    url='https://github.com/lucioveloso/tail-toolkit',
    scripts=['bin/tt'],
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=requires,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    ),
)

setup(**setup_options)
