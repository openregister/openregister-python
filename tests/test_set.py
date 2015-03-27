from entry import Entry


def test_tags_are_a_set():
    entry = Entry(fields={'latitude', 'longitude'})
    assert entry.fields == {'latitude', 'longitude'}

    entry = Entry(fields={'latitude', 'longitude', 'altitude'})
    assert entry.fields == {'altitude', 'latitude', 'longitude'}

    entry = Entry(fields={
        'longitude',
        'latitude',
        'latitude',
        'longitude',
        'latitude',
        'longitude'
    })
    assert entry.fields == {'latitude', 'longitude'}
