#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    desc = f.read()

setup(
    name='NMapify',
    version='0.2',
    description='NMapify is a Python tool that creates mind maps to visualize network layouts using Nmap. It also generates test cases for each identified port to assist pentesters in conducting efficient network pentests.',
    long_description=desc,
    long_description_content_type='text/markdown',
    author='Parimal Shaw',
    license='MIT license',
    url='https://github.com/Parimal-shaw/NMapify',
    install_requires=[
        'pyfiglet==0.8.post1',
        'PyYAML==6.0',
        'rich==13.3.2'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Topic :: Security',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    python_requires='>=3.4',
    entry_points={
        'console_scripts': [
            'NMapify = NMapify:main',
            'nmapify = NMapify:main'
        ]
    },
    keywords=['NMapify', 'network', 'nmap', 'pentesting', 'security'],
)
