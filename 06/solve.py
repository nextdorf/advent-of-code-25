#!/usr/bin/env python

import numpy as np
from pathlib import Path

with open(Path(__file__).parent / 'secret.input') as f:
  ls = f.read().splitlines()
  nums = np.array([list(map(int, l.split())) for l in ls[:-1]])
  ops = ''.join(ls[-1].split())

ys = []
for xs, op in zip(nums.T, ops):
  match op:
    case '+':
      ys.append(xs.sum().item())
    case '*':
      ys.append(xs.prod().item())
    case _:
      raise ValueError(op)
y = sum(ys)
print(y)
