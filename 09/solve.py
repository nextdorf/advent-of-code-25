#!/usr/bin/env python

import numpy as np
from pathlib import Path

with open(Path(__file__).parent / 'secret.input') as f:
  coords = np.array([list(map(int, l.split(','))) for l in f.read().splitlines()])

max_area = 0
for i,x in enumerate(coords):
  for y in coords[i+1:]:
    area = (abs(x-y) + 1).prod().item()
    if area > max_area:
      max_area = area

print(max_area)
