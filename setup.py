#!/usr/bin/env python
from setuptools import find_packages, setup

with open('README.md') as fh:
    long_description = fh.read()

if __name__ == "__main__":
    setup(
        name='py_arkose_generator',
        version='0.0.0.2',
        packages=find_packages(),
        install_requires=['pycryptodome', 'mmh3'],
        long_description_content_type='text/markdown',
        long_description=long_description,
        url='https://github.com/Zai-Kun/py-arkose-token-generator/tree/main',
    )
