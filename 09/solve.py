#!/usr/bin/env python

import numpy as np
from pathlib import Path

with open(Path(__file__).parent / 'secret.input') as f:
  coords = np.array([list(map(int, l.split(','))) for l in f.read().splitlines()])

# def enumerate_and_skip(it, skip=0):
#   eit = enumerate(it)
#   for _ in zip(range(skip), eit):
#     pass
#   yield from eit


def part_one():
  max_area = 0
  for i,x in enumerate(coords):
    for y in coords[i+1:]:
      area = (abs(x-y) + 1).prod().item()
      if area > max_area:
        max_area = area
  return max_area


def part_two(): # Too high
  coords_loop = np.concat([coords, coords[:1]])
  lines = np.stack([coords_loop[:-1], coords_loop[1:]], axis=1)

  max_area = abs(np.diff(coords, axis=0)).max().item()
  for i,x in enumerate(coords):
    # for j,y in enumerate_and_skip(coords, i+1):
    for y in coords[i+1:]:
      area = (abs(x-y) + 1).prod().item()
      if area > max_area:
        # Check that no line goes through the rect:
        xy = np.stack((x, y))
        does_not_cross = True
        for l in lines:
          does_not_cross = (
                (l[:, 0] <= xy[:, 0]).all()
            or  (l[:, 0] >= xy[:, 0]).all()
            or  (l[:, 1] <= xy[:, 1]).all()
            or  (l[:, 1] >= xy[:, 1]).all()
          ).item()
          if not does_not_cross:
            break
        if does_not_cross:
          max_area = area
  return max_area



print('Part 1', part_one())
print('Part 2', part_two())


