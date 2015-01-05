# Thingstance

[![Build Status](https://travis-ci.org/thingstance/thingstance.svg?branch=master)](https://travis-ci.org/thingstance/thingstance)

[![Coverage Status](https://img.shields.io/coveralls/thingstance/thingstance.svg)](https://coveralls.io/r/thingstance/thingstance)

A uniform, immutable data store, addressable by its contents, with properties and types informed by [schema.org/Thing](http://schema.org/Thing).

# Thing

A Thing may be addressed using a unique identifier `uid` generated from the [git-hash](http://git-scm.com/book/en/v2/Git-Internals-Git-Objects) value for the JSON serialization of its contents.

## Thingstance

A Thingstance is a wrapper for a [Thing](#thing), holding additional metadata such as:

* `type` &mdash; a [Type](#types) to group Things, and enumerate a list of expected fields.
* `name` &mdash; a human-readable name for the Thing, which may used to form a [Semantic URL](http://en.wikipedia.org/wiki/Semantic_URL#Slug)
* `tags` &mdash; one or more informal tags for grouping Things.

<a href="https://www.flickr.com/photos/psd/15802043048" title="IMG_20141210_100039 by Paul Downey, on Flickr"><img src="https://farm8.staticflickr.com/7493/15802043048_42c66fa262.jpg" width="375" height="500" alt="IMG_20141210_100039"></a>

## Types ##

The fields expected for a Thing may be defined by assigning a type. For example, a `Thing` with a type of `Location` is expected to have the following fields:

* [longitude](http://schema.org/longitude)
* [latitude](http://schema.org/latitude)

A Thing with a type of `PostalAddress` should have the following fields:

* [streetAddress](http://schema.org/streetAddress)
* [addressLocality](http://schema.org/addressLocality)
* [addressRegion](http://schema.org/addressRegion)
* [addressCountry](http://schema.org/addressCountry)
* [postalCode](http://schema.org/postalCode)
* location &mdash; the uid of the Thing describing the `Location`

## Fields ##

A thing is a set of fields, and the name used for a field is used consistently, for example a field with the name [postalCode](http://schema.org/postalCode) will always indicate the postal code value, regardless of its context, or the type of thing where it appears.

## Datatypes ##

A datatype may be used to validate a field value, such as:

* `String`
* `Float`
* `DateTime`
* `Markdown`
* `Link`

When defining a property, the datatype may be qualified by a single suffix character:

* `!` &mdash; the field is required
* `*` &mdash; the field is a list

## Links

A `Link` may be qualified by the allowed type:

* `Link:Location`

A link to a `Thing` may be identified by a relative link using its `uid`, a link to another `Thing` may be a relative link, or the URL of the place on The Web where it may be resolved, eg. a 

Datatype   |  Link value                            | URL dereferenced
-----------|----------------------------------------|--------------------------------------------
Link:Court | `9e26..5bdb965b21b`                    | `/Court/9e26..5bdb965b21b.json`
Link:Thing | `/Thing/9e26..5bdb965b21b`             | `/Thing/9e26..5bdb965b21b.json`
Link:Court | `/Courts/St-Albans`                    | `https://example.org/Courts/St-Albans.json`
Link:Court | `https://example.org/Courts/St-Albans` | `https://example.org/Courts/St-Albans.json`

## Representations

The canonical format for a Thing is sorted, JSON, but other representations can hold a Thing with fidelity:

* .yaml - a YAML serialisation of the JSON [jsontoyaml](http://jsontoyaml.com/#python)
* .txt - a plain text version compatible with [TiddlyWeb](http://tiddlyweb.org)

A single Thing may be converted into other representations, dependent upon its type, such as:

* .vcf - a vcard for a Person, Place or PostalAddress
* .ics - a calendar event for a time

## Stores

Things and Thingstance data models are independent of how they may be stored, but are intended to easily map to git, key-stores such as mongodb, and redis, relational database tables, and conventional filesystems.
