#!/usr/bin/env python

# This file is public domain via CC0:
# <https://creativecommons.org/publicdomain/zero/1.0/>

import os
import sys

from setuptools import setup, find_packages

import versioneer


with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as f:
 long_description = f.read()


setup(
 name="ezpyi",
 version=versioneer.get_version(),
 description="A wrapper for PyInstaller that simplifies its usage.",
 long_description=long_description,
 long_description_content_type="text/markdown",
 url="https://code.s.zeid.me/ezpyi",
 author="S. Zeid",
 author_email="support+ezpyi@s.zeid.me",
 license="X11 License:  https://tldrlegal.com/license/x11-license",
 classifiers=[
  "Development Status :: 3 - Alpha",
  "Environment :: Console",
  "Intended Audience :: Developers",
  "Natural Language :: English",
  "Programming Language :: Python :: 2",
  "Topic :: Software Development :: Libraries :: Python Modules",
 ],
 packages=find_packages(),
 install_requires=["pyinstaller"],
 entry_points={
  "console_scripts": [
   "ezpyi=ezpyi.__main__:main",
   "ezpyi%d=ezpyi.__main__:main" % sys.version_info.major,
   "ezpyi%d.%d=ezpyi.__main__:main" % (sys.version_info.major, sys.version_info.minor),
  ]
 },
 cmdclass=versioneer.get_cmdclass(),
)
