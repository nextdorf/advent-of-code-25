#!/usr/bin/env python

import numpy as np
from pathlib import Path

with open(Path(__file__).parent / 'secret.input') as f:
  grid = [l.strip() for l in f.readlines()]

dims = (len(grid), len(grid[0]))
count = 0
for i in range(dims[0]):
  for j in range(dims[1]):
    if (x := grid[i][j]) != '@':
      continue
    adj_idx = [ (a, b)
      for a, b in (
        (i-1, j-1), (i, j-1), (i+1, j-1),
        (i-1, j),             (i+1, j),
        (i-1, j+1), (i, j+1), (i+1, j+1)
      )
      if a in range(dims[0]) and b in range(dims[1])
    ]
    n_adj_forklifts = sum([x=='@' for i, j in adj_idx for x in grid[i][j]])
    if n_adj_forklifts < 4:
      count+=1
print(count)


