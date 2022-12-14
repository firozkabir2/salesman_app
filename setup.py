# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in salesman_app/__init__.py
from salesman_app import __version__ as version

setup(
	name="salesman_app",
	version=version,
	description="Salesman management System",
	author="Firoz Kabir",
	author_email="firoz.sysable@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
