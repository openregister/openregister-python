from openregister import Item


def test_tags_are_a_set():
    item = Item(fields={'latitude', 'longitude'})
    assert item.fields == {'latitude', 'longitude'}

    item = Item(fields={'latitude', 'longitude', 'altitude'})
    assert item.fields == {'altitude', 'latitude', 'longitude'}

    item = Item(fields={
        'longitude',
        'latitude',
        'latitude',
        'longitude',
        'latitude',
        'longitude'
    })
    assert item.fields == {'latitude', 'longitude'}
