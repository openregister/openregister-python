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
    assert entry.json == '{}'
    assert entry.hash == "9e26dfeeb6e641a33dae4961196235bdb965b21b"
    assert entry.hashkey == "tytn73vw4za2gpnojfqrsyrvxw4wlmq3"

    entry.foo = "Foo Value"
    assert entry.json == '{"foo":"Foo Value"}'
    assert entry.hash == "257b86bf0b88dbf40cacff2b649f763d585df662"
    assert entry.hashkey == "ev5ynpylrdn7idfm74vwjh3whvmf35tc"

    entry.bar = "こんにちは、元気ですか"
    assert entry.json == '{"bar":"こんにちは、元気ですか","foo":"Foo Value"}'
    assert entry.hash == "d8d2a8d65415145e4ca092af80cc4c6bfa34519c"
    assert entry.hashkey == "3djkrvsucukf4tfaskxybtcmnp5dium4"
