representations = ['json', 'primitive', 'txt', 'yaml']

for r in representations:
    m = __import__('thingstance.representations.'+r)
