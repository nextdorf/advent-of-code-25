#!/usr/bin/env python

import numpy as np
from pathlib import Path

with open(Path(__file__).parent / 'secret.input') as f:
  rs = [tuple(map(int, r.split('-'))) for r in f.read().split(',')]

# I first found all multiplets instead of only doubles
# max_id_len = len(str(np.max(rs).item()))
# ds = {i: tuple(j for j in range(1, i) if not (i % j)) for i in range(1, max_id_len+1)}
# invalids = []
# for a, b in rs:
#   for s in map(str, range(a, b+1)):
#     l = len(s)
#     for d in ds[l]:
#       if s == s[:d] * (l//d):
#         # print(s)
#         invalids.append(int(s))

invalids = []
for a, b in rs:
  i = a
  while i <= b:
    s = str(i)
    l = len(s)
    if l % 2 == 0:
      if s == s[:l//2] * 2:
        invalids.append(i)
      i+=1
    else:
      i = 10**l

# unique_invalids = list(set(invalids))
# print(*unique_invalids, sep='\n')
# sum_invalids = sum(unique_invalids)
sum_invalids = sum(invalids)
print(sum_invalids)

