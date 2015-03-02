#!/usr/bin/env python
# coding=utf-8
import os, sys, platform
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

# get version infomation
exec(open('./version.py').read())

# get flatform python version and requirements
if sys.version_info[0] == 3:
    file_requirements = './requirements/requirements3.txt'
else:
    file_requirements = './requirements/requirements.txt'

with open(file_requirements) as text_requirements:
    requirements = [line for line in text_requirements]

setup(
    name = "funds",
    version = version,
    description = "funds",
    author = "zhanglianxiang",
    license = "LGPL",
    install_requires = requirements,
    packages = find_packages(),
    scripts = ["script/test.py"],
    zip_safe = False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
        ],
    )

