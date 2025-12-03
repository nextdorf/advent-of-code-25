#!/usr/bin/env python

import numpy as np
from pathlib import Path

with open(Path(__file__).parent / 'secret.input') as f:
  bat_banks = np.array([list(map(int, l.strip())) for l in f.readlines()])

def sum_jolts(n):
  jolts = []
  dot_vec = 10**np.arange(n)[::-1]
  for bank in bat_banks:
    idxs = []
    for i in range(n):
      j_prev = idxs[-1] if idxs else -1
      j = j_prev+1 + np.argmax(bank[j_prev+1 : len(bank)-n+i+1]).item()
      idxs.append(j)
    x = (bank[idxs] @ dot_vec).item()
    jolts.append(x)

  res = sum(jolts)
  return res

print('Part 1:', sum_jolts(2))
print('Part 2:', sum_jolts(12))


