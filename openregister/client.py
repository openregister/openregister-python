import os
import requests
import json
from openregister.item import Item


class Client(object):

    """
    Access register items from an openregister server.
    """

    def __init__(self, logger=None, config={}):
        self.logger = logger
        self._config = config

    def config(self, name, suffix):
        "Return config variable value, defaulting to environment"
        var = '%s_%s' % (name, suffix)
        var = var.upper().replace('-', '_')
        if var in self._config:
            return self._config[var]
        return os.environ[var]

    def get(self, url, params=None):
        response = requests.get(url, params=params)
        if self.logger:
            self.logger.info("GET: %s [%s] %s" % (
                response.url, response.status_code, response.text))
        return response

    def item(self, register, value):
        response = self.get('%s/%s/%s.json' % (
            self.config(register, 'register'),
            register,
            value))
        json = response.json()
        item = Item()
        item.primitive = json['entry']
        return item

    def index(self, index, field, value):
        "Search for records matching a value in an index service"
        params = {
            "q": value,
            # search index has '_' instead of '-' in field names ..
            "q.options": "{fields:['%s']}" % (field.replace('-', '_'))
        }

        response = self.get(self.config(index, 'search_url'), params=params)
        results = [hit['fields'] for hit in response.json()['hits']['hit']]

        for result in results:
            for key in result:
                result[key.replace('_', '-')] = result.pop(key)

        return results
