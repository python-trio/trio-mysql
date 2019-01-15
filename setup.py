#!/usr/bin/env python
import io
from setuptools import setup, find_packages

version_tuple = __import__('trio_mysql').VERSION
version = __import__('trio_mysql').VERSION_STRING

with io.open('./README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name="trio_mysql",
    version=version,
    url='https://github.com/python-trio/trio-mysql/',
    author='Matthias Urlichs',
    author_email='matthias@urlichs.de',
    url='https://github.com/PyMySQL/PyMySQL/',
    project_urls={
        "Documentation": "https://trio_mysql.readthedocs.io/",
    },
    description='Pure Python MySQL Driver',
    long_description=readme,
    license="MIT",
    install_requires=[
        "trio",
        "cryptography",
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    packages=find_packages(exclude=['tests*', 'trio_mysql.tests*']),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Database',
        'Framework :: Trio',
    ],
    keywords="MySQL",
)
