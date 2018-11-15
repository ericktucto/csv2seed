#!/usr/bin/env python
from distutils.core import setup

setup(
    name='csv2seed',
    version="0.1.0",
    description='CSV file converter to Laravel Seeders',
    author='Erick Tucto',
    author_email='erick.tucto@outlook.com',
    url='https://ericktucto.com',
    keywords=['csv', 'laravel', 'seeders', 'seed', 'converter', 'generator'],
    packages=['csv2seed'],
    entry_points={
        'console_scripts': ['csv2seed = csv2seed.cli:main']
    },
    licence='MIT'
)
