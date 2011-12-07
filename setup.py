# -*- coding: utf-8 -*-
import os, sys
from setuptools import setup, find_packages

sys.path.insert(0, os.path.abspath("src"))

import whooshfdw

classifiers = [
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python",
    "Programming Language :: SQL",
    "Topic :: Database :: Database Engines/Servers",
]

requires = ['setuptools',
            'whoosh']
setup(
    name='whooshfdw',
    version=whooshfdw.__version__,
    description='whooshfdw is a PostgreSQL fdw of whoosh text search engine.',
    long_description=open("README.rst").read(),
    classifiers=classifiers,
    keywords=['PostgreSQL','fdw','text search'],
    author='WAKAYAMA shirou',
    author_email='shirou.faw at gmail.com',
    url='',
    license='BSD License',
    install_requires=requires,
    data_files=[('sql',['sql/init.sql','sql/query.sql'])],
    package_dir={'': 'src'},
    packages = [
        'whooshfdw',
        ],
)

