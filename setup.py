# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages
from utils.__version__ import __version__

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name="utils",
	version=__version__,
	description="Utils is a collection of common Python functions and classes",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/misaka-ink/utils",
	author="Smiling Xinyi",
	author_email="smilingxinyi@gmail.com",
	license="MIT",
	keywords="utils",
	packages=find_packages(exclude=["docs/*", "test/*", "test*"]),
	install_requires=[]
)
