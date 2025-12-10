#!/usr/bin/env python

import numpy as np
from pathlib import Path
import itertools

with open(Path(__file__).parent / 'secret.input') as f:
  lights, buttons, joltage = [], [], []
  for l in f.read().splitlines():
    ns = l.split()
    lights.append(int(ns[0][1:-1][::-1].replace('.', '0').replace('#', '1'), base=2))
    buttons.append([(2**np.array(list(map(int, x[1:-1].split(','))))).sum().item() for x in ns[1:-1]])
    joltage.append(list(map(int, ns[-1][1:-1].split(','))))

def iter_powerset(xs):
  for i in range(len(xs) + 1):
    yield from itertools.combinations(xs, i)

min_counts = []
for l, bts in zip(lights, buttons):
  for bs in iter_powerset(bts):
    x = l
    for bt in bs:
      x ^= bt
    if not x:
      min_counts.append(len(bs))
      break
min_count = sum(min_counts)


print(min_count)
