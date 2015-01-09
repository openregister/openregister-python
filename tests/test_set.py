from thingstance import Thing


def test_tags_are_a_set():
    thing = Thing(fields={'latitude', 'longitude'})
    assert thing.fields == {'latitude', 'longitude'}

    thing = Thing(fields={'latitude', 'longitude', 'altitude'})
    assert thing.fields == {'altitude', 'latitude', 'longitude'}

    thing = Thing(fields={
        'longitude',
        'latitude',
        'latitude',
        'longitude',
        'latitude',
        'longitude'
    })
    assert thing.fields == {'latitude', 'longitude'}
