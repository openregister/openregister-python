representations = {}

for r in ['csv', 'json', 'primitive', 'tsv', 'txt', 'yaml']:
    representations[r] = __import__('thingstance.representations.'+r)
