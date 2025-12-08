#!/usr/bin/env python

import numpy as np
from pathlib import Path

with open(Path(__file__).parent / 'secret.input') as f:
  coords = np.array([list(map(int, l.split(','))) for l in f.read().splitlines()])

# # Too Slow:
# def enumerate_and_skip(it, skip=0):
#   eit = enumerate(it)
#   for _ in zip(range(skip), eit):
#     pass
#   yield from eit

# clusters = np.arange(len(coords))
# for _ in range(10):
#   a, b, dist = None, None, np.inf
#   for i, x in enumerate(coords):
#     for j, y in enumerate_and_skip(coords, i+1):
#       if same_cluster := clusters[i] == clusters[j]:
#         continue
#       if (xy_dist := np.linalg.norm(x - y)) < dist:
#         a, b, dist = i, j, xy_dist
#   clusters[b] = clusters[a]

# unique_clusters = {i.item() for i in clusters}


def part_one():
  all_norms = np.linalg.norm(np.expand_dims(coords, 1) - np.expand_dims(coords, 0), axis=-1)
  idxs = np.array([(i, j) for i in range(len(coords)) for j in range(i+1, len(coords))])

  norms = all_norms[*idxs.T]

  closest_idxs = idxs[np.argsort(norms)[:1000]]

  clusters = np.arange(len(coords))

  for a, b in closest_idxs:
    clusters[clusters == clusters[b]] = clusters[a]
  unique_clusters = {i.item() for i in clusters}

  cluster_counts = {c: sum(clusters==c).item() for c in unique_clusters}
  sorted_sizes = sorted(cluster_counts.values())
  res = np.prod(sorted_sizes[-3:]).item()
  return res

def part_two():
  all_norms = np.linalg.norm(np.expand_dims(coords, 1) - np.expand_dims(coords, 0), axis=-1)
  idxs = np.array([(i, j) for i in range(len(coords)) for j in range(i+1, len(coords))])

  norms = all_norms[*idxs.T]

  closest_idxs = idxs[np.argsort(norms)]

  clusters = np.arange(len(coords))

  unique_clusters = {}
  last_a, last_b = None, None
  for a, b in closest_idxs:
    clusters[clusters == clusters[b]] = clusters[a]
    unique_clusters = {i.item() for i in clusters}
    if len(unique_clusters) == 1:
      last_a, last_b = a, b
      break
  x, y = coords[[last_a, last_b], :]
  res = (x[0] * y[0]).item()

  return res


print('Part 1:', part_one())
print('Part 1:', part_two())


