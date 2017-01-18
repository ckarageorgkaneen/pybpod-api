#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re

version = ''
with open('pybpodapi/__init__.py', 'r') as fd: version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                                                                      fd.read(), re.MULTILINE).group(1)
if not version:
	raise RuntimeError('Cannot find version information')

requirements = [
	'pyserial',
	'logging-bootstrap',
]

setup(
	name='pybpod-api',
	version=version,
	description="""BPod Python API""",
	author=['Joshua Sanders', 'Carlos Mão de Ferro', 'Ricardo Ribeiro'],
	author_email=['joshua21@gmail.com', 'cajomferro@gmail.com', 'ricardojvr@gmail.com'],
	license='The MIT License (MIT) Copyright 2017 Champalimaud Foundation',
	url='https://bitbucket.org/fchampalimaud/pybpod-api',
	include_package_data=True,
	packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples', 'deploy', 'reports']),
	# install_requires=requirements,
)
