#!/usr/bin/env python3

# see http://bugs.python.org/issue8876
# this is just a quick hack so we can test build in vagrant
import os
if os.environ.get('USER','') == 'vagrant':
  del os.link

from setuptools import setup, find_packages

def requirements():
    with open('./requirements/production.txt', 'r') as f:
        return [l.strip('\n') for l in f if l.strip('\n') and not l.startswith('#')]

setup(name='openregister',
      version='0.5.0',
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
      install_requires=requirements(),
)
