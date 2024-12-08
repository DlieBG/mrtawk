# -*- coding: utf-8 -*-
"""
mrtawk - Advanced Anomaly Detection in Internet Routing
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <mail@bschwer.ing>
"""
from setuptools import find_packages, setup

setup(
    name='mrtawk',
    version='0.1.0',
    description='',
    url='https://git.univ.leitwert.net/imprj/01-bgp-testbed/mrtawk',
    author='Benedikt Schwering',
    author_email='mail@bschwer.ing',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pydantic',
        'click',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'mrtawk=src.main:cli',
        ],
    },
)
