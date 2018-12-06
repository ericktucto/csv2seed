#!/usr/bin/env python
from setuptools import setup
from os.path import dirname, abspath, join

_here = abspath(dirname(__file__))
with open(join(_here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='csv2seed',
    version='0.2.0',

    url='https://github.com/ErickTucto/csv2seed',
    description='CSV file converter to Laravel Seeders',
    long_description=long_description,
    keywords=['csv', 'laravel', 'seeders', 'seed', 'converter', 'generator'],

    license='MIT',

    author='Erick Tucto',
    author_email='erick.tucto@outlook.com',

    packages=['csv2seed'],
    entry_points={
        'console_scripts': ['csv2seed=csv2seed.cli:main']
    }
)
