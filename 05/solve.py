#!/usr/bin/env python

import numpy as np
from pathlib import Path

with open(Path(__file__).parent / 'secret.input') as f:
  s = f.read()
  sep = s.find('\n\n')
  to_range = lambda a, b: range(a, b+1)
  ranges = [to_range(*map(int, l.split('-'))) for l in s[:sep].splitlines()]
  available_ids = list(map(int, s[sep+2:].splitlines()))

fresh_ids = [jd for jd in available_ids if any(jd in r for r in ranges)]
count_fresh_ids = len(fresh_ids)
print(count_fresh_ids)



