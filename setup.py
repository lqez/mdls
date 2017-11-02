#!/usr/bin/env python
from setuptools import setup
from setuptools import find_packages
import re

with open('mdls/__init__.py') as f:
    data = re.search(r'\(\s*(\d*).\s*(\d*).\s*(\d)*\)', f.read())
    version = ".".join([data.group(1), data.group(2), data.group(3)])
assert version

classifiers = [
    'Topic :: Terminals',
    'Topic :: Utilities',
    'Environment :: Console',
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'License :: OSI Approved :: MIT License',
]

setup(
    name='mdls',
    version=version,
    packages=find_packages(),
    zip_safe=True,
    author='Park Hyunwoo',
    author_email='ez.amiryo' '@' 'gmail.com',
    maintainer='Park Hyunwoo',
    maintainer_email='ez.amiryo' '@' 'gmail.com',
    url='http://github.com/lqez/mdls',
    description='Markdown list sorter',
    classifiers=classifiers,
    test_suite='mdls.test',
    entry_points={
        'console_scripts': [
            'mdls = mdls.cmd:main',
        ],
    },
)