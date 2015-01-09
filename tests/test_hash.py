from thingstance import Thing


def test_thing_hash():
    thing = Thing()

    #
    # $ /bin/echo '{}\c' > x
    # $ git add x ; git commit -m"x" x
    # $ git hash-object x
    #
    assert thing.hash == "9e26dfeeb6e641a33dae4961196235bdb965b21b"

    #
    # $ /bin/echo '{"foo": "Foo Value"}\c' > y
    # $ git add y ; git commit -m"y" y
    # $ git hash-object y
    #
    thing.foo = "Foo Value"
    assert thing.json == '{"foo": "Foo Value"}'
    assert thing.hash == "52664e0e405d51dad2d6c0e2979b4e1377e42abc"

    #
    # $ /bin/echo '{"bar": "こんにちは、元気ですか", "foo": "Foo Value"}\c' > z
    # $ git add z ; git commit -m"z" z
    # $ git hash-object z
    #
    thing.bar = "こんにちは、元気ですか"
    assert thing.json == '{"bar": "こんにちは、元気ですか", "foo": "Foo Value"}'
    assert thing.hash == "9e8ef586772127778e1a3ac05bfd16bd20c5e57a"
