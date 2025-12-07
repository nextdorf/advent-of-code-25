#!/usr/bin/env python

import numpy as np
from pathlib import Path

with open(Path(__file__).parent / 'secret.input') as f:
  field = f.read().splitlines()
  start_idx = (0, field[0].find('S'))

def find_all(s: str, sub: str):
  idxs = []
  while (i := s.find(sub, idxs[-1]+1 if idxs else 0)) >= 0:
    idxs.append(i)
  return tuple(idxs)

beam: np.ndarray = (np.arange(len(field[1])).reshape((1, -1)) == start_idx[1]).astype(int)

count = 0
for i in range(2, len(field), 2):
  idxs = np.array(find_all(field[i], '^'))
  b = np.array(beam[-1], copy=True)
  hits = b[idxs] != 0
  count += hits.sum()
  b[idxs-1] += beam[-1, idxs]
  b[idxs] = 0
  b[idxs+1] += beam[-1, idxs]
  beam = np.concat((beam, [b]))

def part_one():
  return count

def part_two():
  return beam[-1].sum()


print('Part 1:', part_one())
print('Part 2:', part_two())


# for i, l in enumerate(field):
#   for j, x in enumerate(l):
#     if x != '.':
#       s = x
#     elif beam[i//2, j]:
#       s = '|'
#     else:
#       s = '.'
#     print(s, end='')
#   print()



