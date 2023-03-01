#!/usr/bin/env python

from setuptools import setup, find_packages

VER = "0.1.1"

setup(
    name="matcha",
    version=VER,
    author="Andrew J. Mogan",
    author_email="andrew.mogan@colostate.edu",
    description="A package for matching CRT hit information with TPC tracks.",
    url="https://github.com/andrewmogan/matcha",
    packages=find_packages(where="src"), 
    package_dir={"":"src"},
    install_requires=['scikit-learn'],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
