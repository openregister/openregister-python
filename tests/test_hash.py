from thingstance import Thing

# to confirm the hash of a Thing matches the git-hash value:
#
# $ /bin/echo '{}\c' > x
# $ git add x ; git commit -m"x" x
#
# $ git hash-object | python
# 9e26dfeeb6e641a33dae4961196235bdb965b21b
#
# the RFC 3548 Base 32 encoded version is shorter and readable
#
# bin/base32 $(git hash-object)


def test_thing_hash():

    thing = Thing()
    assert thing.hash == "9e26dfeeb6e641a33dae4961196235bdb965b21b"
    assert thing.hashkey == "tytn73vw4za2gpnojfqrsyrvxw4wlmq3"

    thing.foo = "Foo Value"
    assert thing.json == '{"foo": "Foo Value"}'
    assert thing.hash == "52664e0e405d51dad2d6c0e2979b4e1377e42abc"
    assert thing.hashkey == "kjte4dsalvi5vuwwydrjpg2ocn36ikv4"

    thing.bar = "こんにちは、元気ですか"
    assert thing.json == '{"bar": "こんにちは、元気ですか", "foo": "Foo Value"}'
    assert thing.hash == "9e8ef586772127778e1a3ac05bfd16bd20c5e57a"
    assert thing.hashkey == "t2hplbtxeetxpdq2hlafx7iwxuqmlzl2"
