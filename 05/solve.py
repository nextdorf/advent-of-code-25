#!/usr/bin/env python

import numpy as np
from pathlib import Path

with open(Path(__file__).parent / 'secret.input') as f:
  s = f.read()
  sep = s.find('\n\n')
  to_range = lambda a, b: range(a, b+1)
  ranges = [to_range(*map(int, l.split('-'))) for l in s[:sep].splitlines()]
  available_ids = list(map(int, s[sep+2:].splitlines()))

def part_one():
  fresh_ids = [jd for jd in available_ids if any(jd in r for r in ranges)]
  count_fresh_ids = len(fresh_ids)
  return count_fresh_ids

def part_two():
  # # This ansatz hangs Python:
  # fresh_ids = set()
  # for r in ranges:
  #   fresh_ids.update(r)

  disjunct = []
  for r in ranges:
    a, b = r.start, r.stop
    overlappings_idx = [idx for idx, (x, y) in enumerate(disjunct) if not (b < x or a > y)]
    overlappings = [disjunct[i] for i in overlappings_idx]
    new_range = (min(a, a, *(x for x, y in overlappings)), max(b, b, *(y for x, y in overlappings)))
    # new_range = (a, b)
    disjunct = [r for i, r in enumerate(disjunct) if not i in overlappings_idx]
    disjunct.append(new_range)

  fresh_ranges = [range(a, b) for a, b in disjunct]
  count_fresh_ids = sum(map(len, fresh_ranges))
  return count_fresh_ids


print('Part 1: ', part_one())
print('Part 2: ', part_two())

