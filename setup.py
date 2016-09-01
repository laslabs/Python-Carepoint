# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from setuptools import setup
from setuptools import find_packages
from tests import Tests


PACKAGE_NAME = 'carepoint'
VERSION = '0.0.1.0'


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    packages=find_packages(exclude=('tests', )),
    cmdclass={'test': Tests},
    tests_require=[
        'pysqlite',
        'sqlalchemy',
        'xmlrunner',
        'mock',
    ],
    install_requires=[
        # 'pyodbc',
        'pysmb',
    ]
)
