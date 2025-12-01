#!/usr/bin/env python

import numpy as np
from pathlib import Path

with open(Path(__file__).parent / 'secret.input') as f:
  nums = [50] + [(dict(R=1,L=-1)[si[0]] * int(si[1:])) % 100 for si in f.readlines() if si]

cum_nums = np.cumsum(nums) % 100
password = (cum_nums == 0).sum().item()
print(password)

