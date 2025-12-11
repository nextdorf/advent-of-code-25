#!/usr/bin/env python

import numpy as np
from pathlib import Path

with open(Path(__file__).parent / 'secret.input') as f:
  gr = {a: {'nodes': b.split()} for a,b in (l.split(': ') for l in f.read().splitlines())}

def init_count_attr(g: dict, target='out'):
  g.setdefault(target, {})
  g[target]['count'] = 1

def set_count_attr(g: dict, start: str):
  x = g[start]
  if not 'count' in x:
    counts = []
    for y in x['nodes']:
      counts.append(set_count_attr(g, y))
    x['count'] = sum(counts)
  return x['count']


init_count_attr(gr)
dist_to_out = set_count_attr(gr, 'you')
print(dist_to_out)


