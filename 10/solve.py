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

def binary_to_vec(x, min_len=0):
  res = []
  for i in (2**j for j in range(64)):
    if i > x:
      break
    res.append(bool(x & i))
  res = np.concat([res, [0]*(min_len-len(res))]).astype(np.int_)
  return res


def part_one():
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
  return min_count

def part_two():
  min_counts = []
  for l, bts, jol in zip(lights, buttons, map(np.array, joltage)):
    c = np.inf
    for bs in iter_powerset(bts):
      x = l
      for bt in bs:
        x ^= bt
      if not x:
        x_vec = binary_to_vec(x)
        jol0 = np.sum([binary_to_vec(b, len(x_vec)) for b in bs], axis=0)
        jol1 = jol
        # TODO: find way of pressing zeros and reaching the left over joltage

    min_counts.append(c)
  min_count = sum(min_counts)
  return min_count


print('Part 1:', part_one())
