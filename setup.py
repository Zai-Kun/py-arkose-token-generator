#!/usr/bin/env python

from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
        name='py_arkose_generator',
        packages=find_packages(),
        install_requires=["mmh3"],
    )
