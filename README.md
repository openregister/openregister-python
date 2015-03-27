# Openregister entry

[![Build Status](https://travis-ci.org/openregister/entry.svg?branch=master)](https://travis-ci.org/openregister/entry) [![Coverage Status](https://img.shields.io/coveralls/openregister/entry.svg)](https://coveralls.io/r/openregister/entry)

A uniform, immutable data store, addressable by its contents, with consistent properties and types.

# Entry

An Entry is a set of [[fields|Field]], addressable by its [[Hash]].

## Field ##

A Field is a named value, where name used for a field is globally unique, to be used consistently across all instances of entries.

Where possible the name used for a field matches, or can be mapped onto properties  example a field with a name of [postalCode](http://schema.org/postalCode) field will always indicate the postal code, regardless of where it appears.

# Hash

An Entry may be addressed using a unique identifier `hash` generated from the [git-hash](http://git-scm.com/book/en/v2/Git-Internals-Git-Objects) value for the JSON serialization of its contents.

## Datatype ##

Each field has a defined `Datatype` which may be used to constrain the field value, for example `String`, `Text`, `Float`, `DateTime`, `Link`, etc.

When defining a field, the datatype may be qualified by a single suffix character:

* `!` &mdash; the field is a required value
* `*` &mdash; the field is a list of values
* `#` &mdash; the field is a set of values

## Link

A `Link` datatype may be qualified by the Tag being referenced:

* `Link:Location`

A link to an `Entry` may be identified by a relative link using its [[Hash]] value, or other value, a link to another `Entry` may be a relative link, or the URL of the place on The Web where it may be resolved, eg. a 

Datatype   |  Link value                            | URL dereferenced
:----------|:---------------------------------------|:-------------------------------------------
Link:Court | `9e26..5bdb965b21b`                    | `/Court/9e26..5bdb965b21b`
Link:Entry | `/Entry/9e26..5bdb965b21b`             | `/Entry/9e26..5bdb965b21b`
Link:Court | `/Courts/St-Albans`                    | `https://example.org/Courts/St-Albans`
Link:Court | `https://example.org/Courts/St-Albans` | `https://example.org/Courts/St-Albans`

## Tag ##

The attributes expected for an Entry may be defined by assigning one or more Tags.

For example, a `Entry` with a type of `Location` should have the following attributes:

* [longitude](http://schema.org/longitude)
* [latitude](http://schema.org/latitude)

and an Entry with a type of `PostalAddress` should have the following attributes:

* [streetAddress](http://schema.org/streetAddress)
* [addressLocality](http://schema.org/addressLocality)
* [addressRegion](http://schema.org/addressRegion)
* [addressCountry](http://schema.org/addressCountry)
* [postalCode](http://schema.org/postalCode)
* location &mdash; the uid of the Entry describing the `Location`

## Representation

The canonical format for a single Entry is sorted, JSON, but other representations can hold a list of Entries with fidelity:

* .yaml - a YAML serialisation of the JSON [jsontoyaml](http://jsontoyaml.com/#python)
* .txt - a plain text version compatible with [TiddlyWeb](http://tiddlyweb.org)

A single Entry may be converted into other representations, dependent upon its type, such as:

* .vcf - a vcard for a Person, Place or PostalAddress
* .ics - a calendar event for a time

## List of Links

A search or other filter may return a list references to Entries represented as a JSON, YAML, [Atom](http://en.wikipedia.org/wiki/Atom_(standard)), or other list of [[Link]] values.

## List of Entries

A bulk operation such as a backup, restore, search or other filter may use a list of things, represented as a JSON, YAML, Atom or other sequence of Entries.

## Store

Entries and Openregister data models are independent of how they may be stored, but are intended to easily map to git, key-stores such as mongodb, and redis, relational database tables, and conventional filesystems.

## Development

Requires Python 3.4:

    $ mkvirtualenv openregister
    $ workon openregister
    (openregister) pip3 install -r requirements.txt
    (openregister)$ make
