#!/usr/bin/env python

import numpy as np
from pathlib import Path

with open(Path(__file__).parent / 'secret.input') as f:
  grid = [l.strip() for l in f.readlines()]

def part_one():
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
  return count

def part_two():
  _grid = [x for x in grid]
  dims = (len(_grid), len(_grid[0]))
  count = 0
  while True:
    movables = []
    for i in range(dims[0]):
      for j in range(dims[1]):
        if (x := _grid[i][j]) != '@':
          continue
        # _grid[i] = _grid[i][:j] + 'x' + _grid[i][j+1:]
        adj_idx = [ (a, b)
          for a, b in (
            (i-1, j-1), (i, j-1), (i+1, j-1),
            (i-1, j),             (i+1, j),
            (i-1, j+1), (i, j+1), (i+1, j+1)
          )
          if a in range(dims[0]) and b in range(dims[1])
        ]
        n_adj_forklifts = sum([x=='@' for i, j in adj_idx for x in _grid[i][j]])
        if n_adj_forklifts < 4:
          count+=1
          movables.append((i, j))
    if movables:
      for i, j in movables:
        _grid[i] = _grid[i][:j] + 'x' + _grid[i][j+1:]
    else:
      break
  return count



print('Part 1', part_one())
print('Part 2', part_two())


