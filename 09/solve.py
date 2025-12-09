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


def gen_orientation(coords=coords):
  '''
  If the lines would form a rectangle then, depending on the direction the lines are defined,
  the number of turns is either 4 rights and 0 lefts or 0 rights and 4 lefts. If onw would extrude
  a smaller rectangle on of the sides, either inwards or outwards, the total number of addtitional
  left turns and right turns would be equal. Without loss of generality, one might start with a
  1x1 rectangle and only add single 1x1 rectangle. It is obvious that any shape might be created
  in that way and that the orientation is an invariant during this building process.

  It further follows that the orientation can be measured by subtracting the number of left turns
  from the number of right turns
  '''
  _coords = np.concat((coords, coords[:2]))
  turns = []
  eps = np.array(((0, 1), (-1, 0)))
  for i in range(len(coords)):
    x, y, z = _coords[[i, i+1, i+2]]
    cross = (y-x) @ eps @ (z-y)
    turns.append(np.sign(cross))
  turns = np.array(turns)
  o = turns.sum().item()
  return o, turns

def gen_normals(coords=coords):
  'The normals point into the insides'
  _coords = np.concat((coords, coords[:1]))
  o, turns = gen_orientation(coords=coords)
  normals = []
  rot = np.array(((0, -1), (1, 0)))
  for i in range(len(coords)):
    x, y = _coords[[i, i+1]]
    n = rot @ (y-x)
    normals.append(n // abs(n).max())
  # normals = np.array(normals) * np.expand_dims(np.sign(o) * turns, 1)
  normals = np.array(normals) * np.sign(o)
  normals.sum(axis=0)
  return normals




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


