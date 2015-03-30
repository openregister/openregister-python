#!/usr/bin/env python3

# see http://bugs.python.org/issue8876
# this is just a quick hack so we can test build in vagrant
import os
if os.environ.get('USER','') == 'vagrant':
  del os.link

from setuptools import setup, find_packages

def requirements():
    with open('./requirements.txt', 'r') as f:
        return [l.strip('\n') for l in f if l.strip('\n') and not l.startswith('#')]

setup(name='openregister-entry',
      version='0.2.0',
      description='Entry model package',
      author='Openregister.org',
      author_email='paul.downey@whatfettle.com',
      url='https://github.com/openregister/entry',
      download_url='https://github.com/openregister/entry',
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
