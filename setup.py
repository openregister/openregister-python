#!/usr/bin/env python3

# see http://bugs.python.org/issue8876
# this is just a quick hack so we can test build in vagrant
import os
if os.environ.get('USER','') == 'vagrant':
  del os.link

from setuptools import setup, find_packages

setup(name='openregister',
      version='0.5.4',
      description='Openregister core package',
      long_description='Python libraries for wrangling register data',
      author='Openregister.org',
      author_email='paul.downey@whatfettle.com',
      url='https://github.com/openregister/openregister-python',
      download_url='https://github.com/openregister/openregister-python',
      packages=find_packages(exclude=['tests']),
      zip_safe=False,
      include_package_data=True,
      license='MIT',
      platforms='any',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3.4',
        ],
      install_requires=[
        'PyYAML>=3.11',
        'pymongo>=2.7.2'
      ]
)
