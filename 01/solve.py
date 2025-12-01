#!/usr/bin/env python

import numpy as np
from pathlib import Path

with open(Path(__file__).parent / 'secret.input') as f:
  num0 = 50
  nums = [(dict(R=1,L=-1)[si[0]] * int(si[1:])) for si in f.readlines() if si]

def part_one():
  cum_nums = np.cumsum([num0] + nums) % 100
  password = (cum_nums == 0).sum().item()
  return password

def part_two():
  clicks = int(num0 == 0)
  x = num0
  for n in nums:
    if n >=0:
      click_inc = (x + n) // 100
    else:
      click_inc = (100 - (x + n)) // 100 - int(x==0)
    clicks += click_inc
    x = (x + n) % 100
  return clicks


print('Part 1:', part_one())
print('Part 2:', part_two())

