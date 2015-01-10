from thingstance import Thing


def test_thing_hash():
    thing = Thing()

    #
    # $ /bin/echo '{}\c' > x
    # $ git add x ; git commit -m"x" x
    # $ git hash-object | python
    # 9e26dfeeb6e641a33dae4961196235bdb965b21b
    # bin/base32 $(git hash-object)
    #
    assert thing.hash == "tytn73vw4za2gpnojfqrsyrvxw4wlmq3"

    #
    # $ /bin/echo '{"foo": "Foo Value"}\c' > y
    # $ git add y ; git commit -m"y" y
    # $ git hash-object y
    # 52664e0e405d51dad2d6c0e2979b4e1377e42abc
    #
    thing.foo = "Foo Value"
    assert thing.json == '{"foo": "Foo Value"}'
    assert thing.hash == "kjte4dsalvi5vuwwydrjpg2ocn36ikv4"

    #
    # $ /bin/echo '{"bar": "こんにちは、元気ですか", "foo": "Foo Value"}\c' > z
    # $ git add z ; git commit -m"z" z
    # $ git hash-object z
    # 9e8ef586772127778e1a3ac05bfd16bd20c5e57a
    #
    thing.bar = "こんにちは、元気ですか"
    assert thing.json == '{"bar": "こんにちは、元気ですか", "foo": "Foo Value"}'
    assert thing.hash == "t2hplbtxeetxpdq2hlafx7iwxuqmlzl2"
