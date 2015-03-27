from entry import Entry

# to confirm the hash of a Entry matches the git-hash value:
#
# $ /bin/echo '{}' > x
# $ git add x ; git commit -m"x" x
# $ git hash-object x
# 0967ef424bce6791893e9a57bb952f80fd536e93
#
# the RFC 3548 Base 32 encoded version is shorter and readable
#
# bin/base32 $(git hash-object x)


def test_entry_hash():

    entry = Entry()
    assert entry.json == '{}\n'
    assert entry.hash == "0967ef424bce6791893e9a57bb952f80fd536e93"
    assert entry.hashkey == "bft66qslzztzdcj6tjl3xfjpqd6vg3ut"

    entry.foo = "Foo Value"
    assert entry.json == '{"foo": "Foo Value"}\n'
    assert entry.hash == "5372dbe0556e453e96000909f45ab626f155bd9f"
    assert entry.hashkey == "knznxycvnzct5fqabee7iwvwe3yvlpm7"

    entry.bar = "こんにちは、元気ですか"
    assert entry.json == '{"bar": "こんにちは、元気ですか", "foo": "Foo Value"}\n'
    assert entry.hash == "f5605fd1dd76899ba506f6d32553f31f3b676b19"
    assert entry.hashkey == "6vqf7uo5o2ezxjig63jsku7td45wo2yz"
