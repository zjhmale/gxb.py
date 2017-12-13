#!/usr/bin/env python
from setuptools import setup

setup(
    name='gxb',
    version='0.1.0',
    packages=['gxb', 'gxb.api'],
    description='GXB Python SDK',
    url='https://github.com/zjhmale/gxb.py',
    author='zjhmale',
    license='MIT',
    author_email='zjhsdtc@gmail.com',
    install_requires=['requests', 'pyOpenSSL', 'ndg-httpsclient', 'pyasn1'],
    keywords='GXB GXShare',
    classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
