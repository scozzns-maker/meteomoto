import json, sys
d = json.load(open(sys.argv[1]))
if isinstance(d, dict) and d.get('error'):
    print('ERROR', d.get('reason'))
    sys.exit()
a = d if isinstance(d, list) else [d]
h = a[0]['hourly']
keys = list(h.keys())
t = h['time']
days = sorted(set(x[:10] for x in t))
nn = {dd: sum(1 for x, v in zip(t, h['temperature_2m']) if x.startswith(dd) and v is not None) for dd in days}
j = t.index(days[0] + 'T12:00')
print('array' if isinstance(d, list) else 'object', len(a), 'keys', keys, 'nonnull T per day', nn,
      '12:00 sample', {k: h[k][j] for k in keys if k != 'time'}, 'elev', a[0].get('elevation'))
