# Openregister python core package

[![Build Status](https://travis-ci.org/openregister/entry.svg?branch=master)](https://travis-ci.org/openregister/entry) [![Coverage Status](https://img.shields.io/coveralls/openregister/entry.svg)](https://coveralls.io/r/openregister/entry)

A uniform, immutable data store, addressable by its contents, with consistent properties and types.

## Item ##

An Item is a set of [fields](#Field), addressable by a [hash](#Hash) of its contents.

## Field ##

A Field is a named value, where name used for a field is globally unique, intended to be used consistently across all instances of entries.

Where possible the name used for a field matches, or can be mapped onto properties. For example, a field with a name of [postcode](http://schema.org/postalCode) will always indicate the postal code, regardless of where it appears.

## Hash ##

An Item may be addressed using a unique identifier `hash` generated from the [git-hash](http://git-scm.com/book/en/v2/Git-Internals-Git-Objects) value for the canonical JSON serialization of its contents.

## Datatype ##

Each field has a defined `Datatype` which may be used to constrain the field value, for example `string`, `text`, `date-time`, `curie`, etc.

When defining a field, the datatype may be qualified by a single suffix character:

* `*` &mdash; the field is a list of values

## Representations

The canonical format for a single Item is sorted JSON with whitespaces removed, but other representations can hold a list of Entries with fidelity:

* .yaml - a YAML serialisation of the JSON [jsontoyaml](http://jsontoyaml.com/#python)
* .txt - a plain text version compatible with [TiddlyWeb](http://tiddlyweb.org)

## Store

Entries and Openregister data models are independent of how they may be stored, but are intended to easily map to git, key-stores such as mongodb, and redis, relational database tables, and conventional filesystems.

## Development

Requires Python 3.4:

    $ mkvirtualenv openregister
    $ workon openregister
    (openregister) make init
    (openregister) make

The MongoDB tests require mongo to be running:

    $ mongod
