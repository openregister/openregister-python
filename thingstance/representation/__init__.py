representations = ['json', 'yaml']

for r in representations:
    m = __import__('thingstance.representation.'+r)
