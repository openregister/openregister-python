from thingstance import Thing

# to confirm the hash of a Thing matches the git-hash value:
#
# $ /bin/echo '{}' > x
# $ git add x ; git commit -m"x" x
# $ git hash-object x
# 0967ef424bce6791893e9a57bb952f80fd536e93
#
# the RFC 3548 Base 32 encoded version is shorter and readable
#
# bin/base32 $(git hash-object x)


def test_thing_hash():

    thing = Thing()
    assert thing.json == '{}\n'
    assert thing.hash == "0967ef424bce6791893e9a57bb952f80fd536e93"
    assert thing.hashkey == "bft66qslzztzdcj6tjl3xfjpqd6vg3ut"

    thing.foo = "Foo Value"
    assert thing.json == '{"foo": "Foo Value"}\n'
    assert thing.hash == "5372dbe0556e453e96000909f45ab626f155bd9f"
    assert thing.hashkey == "knznxycvnzct5fqabee7iwvwe3yvlpm7"

    thing.bar = "こんにちは、元気ですか"
    assert thing.json == '{"bar": "こんにちは、元気ですか", "foo": "Foo Value"}\n'
    assert thing.hash == "f5605fd1dd76899ba506f6d32553f31f3b676b19"
    assert thing.hashkey == "6vqf7uo5o2ezxjig63jsku7td45wo2yz"
