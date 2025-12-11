#!/usr/bin/env python

import numpy as np
from pathlib import Path
import copy

with open(Path(__file__).parent / 'secret.input') as f:
  _gr = {a: {'nodes': b.split()} for a,b in (l.split(': ') for l in f.read().splitlines())}

def init_count_attr(g: dict, target='out'):
  g.setdefault(target, {})
  g[target]['count'] = 1

def new_gr():
  g = copy.deepcopy(_gr)
  init_count_attr(g)
  return g

def set_count_attr(g: dict, start: str, visiting = []):
  if start == 'out':
    return int(not bool(visiting))
  x = g[start]
  if start in visiting:
    visiting = [v for v in visiting if v!=start]
  # if visiting or not 'count' in x:
  if visiting or not 'count' in x:
    counts = []
    for y in x['nodes']:
      counts.append(set_count_attr(g, y, visiting=visiting))
    x['count'] = sum(counts)
  return x['count']


def part_one():
  g = new_gr()
  dist_to_out = set_count_attr(g, 'you')
  return dist_to_out, g

def part_two():
  g = new_gr()
  _dist_to_out = set_count_attr(g, 'svr')
  dist_to_out = set_count_attr(g, 'svr', 'dac fft'.split())
  return dist_to_out, g


print('Part 1:', part_one()[0])
print('Part 2:', part_two()[0])

