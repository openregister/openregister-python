# import pytest
from openregister.client import Client


def test_client_url():
    client = Client(config={
        'ADDRESS_REGISTER': 'https://address.register.example.org'
    })
    assert client.logger is None
    assert client.config('address', 'register') ==\
        'https://address.register.example.org'


#
# @pytest.fixture
# def requests():
#    return requests.get("data")
#
#
# def test_get_register_register(get):
#    url = "http://www.example.com/"
#    text = 'example data'
#    #mock.get(url, text=text)
#    # client = Client()
#    assert text == requests.get(url).text
