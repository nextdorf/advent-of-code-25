#!/usr/bin/env python

import numpy as np
from pathlib import Path

with open(Path(__file__).parent / 'secret.input') as f:
  ls = f.read().splitlines()
  ops = ''.join(ls[-1].split())

def part_one():
  nums = np.array([list(map(int, l.split())) for l in ls[:-1]])
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
  return y

def part_two():
  def calc_y(op, xs):
    match op:
      case '+':
        return sum(xs)
      case '*':
        return np.prod(xs).item()
      case _:
        raise ValueError(op)

  dims = (len(ls)-1, len(ls[0]))
  ys = []
  op_idx = 0
  xs = []
  op = None
  for j in range(dims[1]):
    op = ops[op_idx]
    l = ''
    for i in range(dims[0]):
      l += ls[i][j]
    if l.strip():
      xs.append(int(l))
    else:
      ys.append(calc_y(op, xs))
      xs = []
      op_idx += 1
  ys.append(calc_y(op, xs))
  y = sum(ys)
  return y



print('Part 1', part_one())
print('Part 2', part_two())
