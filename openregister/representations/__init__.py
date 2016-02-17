representations = {}

for r in ['csv', 'json', 'jsonl', 'tsv', 'txt', 'yaml']:
    representations[r] = __import__('openregister.representations.'+r)
