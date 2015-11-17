# Openregister python core

[![Build Status](https://travis-ci.org/openregister/openregister-python.svg?branch=master)](https://travis-ci.org/openregister/openregister-python) [![Coverage Status](https://coveralls.io/repos/openregister/openregister-python/badge.svg?branch=master&service=github)](https://coveralls.io/github/openregister/openregister-python?branch=master)

A python package for representing openregister data in different formats, useful for prototyping registers.

## Dependencies

Requires Python 3, we recommend using a [virtualenv](https://virtualenvwrapper.readthedocs.org/en/latest/):

    $ mkvirtualenv -p python3 openregister
    $ workon openregister

    (openregister) make init
    (openregister) make

The MongoDB store tests require mongo to be running:

    $ mongod
