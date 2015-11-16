from openregister import Item

# to confirm the hash of a Item matches the git-hash value:
#
# $ /bin/echo '{}' > x
# $ git add x ; git commit -m"x" x
# $ git hash-object x
# 0967ef424bce6791893e9a57bb952f80fd536e93
#
# the RFC 3548 Base 32 encoded version is shorter and readable
#
# bin/base32 $(git hash-object x)


def test_item_hash():

    item = Item()
    assert item.json == '{}'
    assert item.hash == "9e26dfeeb6e641a33dae4961196235bdb965b21b"
    assert item.hashkey == "tytn73vw4za2gpnojfqrsyrvxw4wlmq3"

    item.foo = "Foo Value"
    assert item.json == '{"foo":"Foo Value"}'
    assert item.hash == "257b86bf0b88dbf40cacff2b649f763d585df662"
    assert item.hashkey == "ev5ynpylrdn7idfm74vwjh3whvmf35tc"

    item.bar = "こんにちは、元気ですか"
    assert item.json == '{"bar":"こんにちは、元気ですか","foo":"Foo Value"}'
    assert item.hash == "d8d2a8d65415145e4ca092af80cc4c6bfa34519c"
    assert item.hashkey == "3djkrvsucukf4tfaskxybtcmnp5dium4"
