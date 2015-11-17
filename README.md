# Openregister python core

[![Build Status](https://travis-ci.org/openregister/openregister-python.svg?branch=master)](https://travis-ci.org/openregister/openregister-python) [![Coverage Status](https://img.shields.io/coveralls/openregister/openregister-python.svg)](https://coveralls.io/r/openregister/openregister-python)

A python package for representing openregister data in different formats, useful for prototyping registers.

## Dependencies

Requires Python 3:

    $ mkvirtualenv openregister
    $ workon openregister
    (openregister) make init
    (openregister) make

The MongoDB store tests require mongo to be running:

    $ mongod
