#!/usr/bin/env python

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

tests_require = [
]

install_requires = [
]

setup(
    name='nydus',
    version='0.1',
    author='David Cramer',
    author_email='dcramer@gmail.com',
    url='http://github.com/disqus/nydus',
    description = 'Connection utilities',
    packages=find_packages(),
    zip_safe=False,
    install_requires=install_requires,
    dependency_links=[],
    tests_require=tests_require,
    extras_require={'test': tests_require},
    # test_suite='runtests.runtests',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)