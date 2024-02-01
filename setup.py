#!/usr/bin/env python

from distutils.core import setup

setup(name='comp_bio',
      version='0.1.0',
      description='Misc computational biology and computational chemistry stuff. Plus playing with flask and docker again',
      packages=['comp_bio'],
      install_requires=[
          'numpy',
          'matplotlib',
          'pytest'
      ]
)