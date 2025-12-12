#!/usr/bin/env python

import numpy as np
from pathlib import Path

with open(Path(__file__).parent / 'secret.input') as f:
  q = f.read().split('\n\n')
  def get_shape(qi):
    return [[c=='#' for c in s] for s in qi.split()[1:]]
  def get_tree(l):
    _l = l.split()
    x, y = map(int, _l[0][:-1].split('x'))
    cs = np.array(list(map(int, _l[1:])))
    return dict(x = x, y = y, count=cs)
  shapes = np.array(list(map(get_shape, q[:-1])))
  trees = _trees = list(map(get_tree, q[-1].split('\n')))

dof_cost = shapes.sum(axis=(1,2))
for t in trees:
  t['dof'] = (t['x']*t['y'] - t['count'] @ dof_cost).item()

trees = [t for t in trees if t['dof'] >= 0]

count_upper_bound = len(trees)

print(count_upper_bound)
