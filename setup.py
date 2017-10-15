#!/usr/bin/env python
import os

try:
    from setuptools import setup, find_packages
    packages = find_packages(exclude=['tests'])
except ImportError:
    from distutils.core import setup
    packages = ["pylev3"]


setup(
    name="pylev3",
    packages=packages,
    version="1.1.0",
    description="A Python3 Levenshtein distance (re)implementation of pylev",
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       "README.rst")).read(),
    author="hell03end",
    author_email="hell03end@outlook.com",
    url="https://github.com/hell03end/pylev3",
    keywords="Levenshtein texts",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    license="BSD License",
    platforms=["All"],
    python_requires=">=3.3"
)
