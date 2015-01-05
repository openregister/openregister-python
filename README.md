# Thingstance

A uniform, immutable data store, addressable by its contents, with properties and types informed by [schema.org/Thing](http://schema.org/Thing).

A Thingstance is an instance of a [Thing][], with additional metadata such as:

* `type` &mdash; a [Type][#Types] to group Things, and enumerate a list of expected fields.
* `name` &mdash; a human-readable name for the Thing, which may used to form a [Semantic URL](http://en.wikipedia.org/wiki/Semantic_URL#Slug)
* `tags` &mdash; one or more informal tags for grouping Things.

# Thing

A Thing may be addressed using a unique identifier (`uid`), generated from the [git-hash](http://git-scm.com/book/en/v2/Git-Internals-Git-Objects) value for the JSON serialization of its contents.

The `uid` this unique combined with , and an instance of the Thing are known as a Thingstance:

<a href="https://www.flickr.com/photos/psd/15802043048" title="IMG_20141210_100039 by Paul Downey, on Flickr"><img src="https://farm8.staticflickr.com/7493/15802043048_42c66fa262.jpg" width="375" height="500" alt="IMG_20141210_100039"></a>

## Types ##

The fields expected for a Thing may be defined by assigning a Type. For example, a Thing with a type of `Location` is expected to have the following fields:

* [longitude](http://schema.org/longitude)
* [latitude](http://schema.org/latitude)

and a Thing with a type of `PostalAddress` may have the following fields:

* [streetAddress](http://schema.org/streetAddress)
* [addressLocality](http://schema.org/addressLocality)
* [addressRegion](http://schema.org/addressRegion)
* [addressCountry](http://schema.org/addressCountry)
* [postalCode](http://schema.org/postalCode)
* location &mdash; the uid of the Thing describing the `Location`

## Fields ##

A thing is a set of fields, and the name used for a field is used consistently, for example a field with the name [postalCode](http://schema.org/postalCode) will always indicate the postal code value, regardless of its context, or the type of thing where it appears.

## Datatypes ##

A datatype may be used to validate a field value, such as `String`, `Float`, `DateTime`, `Markdown`, `Link:Location`, etc.

## Representations

The canonical format for a Thing is sorted, JSON, but other representations can hold a Thing with fidelity:

* .yaml - a YAML serialisation of the JSON [jsontoyaml](http://jsontoyaml.com/#python)
* .txt - a plain text version compatible with [TiddlyWeb](http://tiddlyweb.org)

A single Thing may be converted into other representations, dependent upon its type, such as:

* .vcf - a vcard for a Person, Place or PostalAddress
* .ics - a calendar event for a time

## Stores

Things and Thingstance data model is independent of how they may be stored, but are intended to easily map to git, key-stores such as mongodb, and redis, relational database tables, and conventional filesystems.
