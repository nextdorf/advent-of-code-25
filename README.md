# Advent of Code 2025

Python solutions for Advent of Code 2025 puzzles. Each day lives in its own folder with the problem statement, my input, and a solver script that prints both puzzle answers.

## Layout
- `01` / `02` / `03`: Day folders containing `README.md` (puzzle text), `secret.input` (my puzzle input), and `solve.py`.
- `LICENSE`: MIT license for this repository.

## Requirements
- Python 3.11+ (tested locally)
- `numpy` (`pip install numpy`)

## Running a day
From the repo root:

```bash
python 01/solve.py
python 02/solve.py
python 03/solve.py
```

Current outputs with the included inputs:
- Day 1: `Part 1: 1154`, `Part 2: 6819`
- Day 2: `Part 1: 13108371860`, `Part 2: 22471660255`
- Day 3: `Part 1: 17142`, `Part 2: 169935154100102`

## Solution notes
- **Day 1 – Secret Entrance (`01/solve.py`)**: Parses dial rotations and uses cumulative sums mod 100 to count times the dial lands on 0 (part 1). Part 2 walks each rotation to count every intermediate click that crosses 0.
- **Day 2 – Gift Shop (`02/solve.py`)**: Reads comma-separated ID ranges. Part 1 filters even-length numbers that are exactly two repeated halves. Part 2 precomputes divisors for each possible digit length and checks whether a number is composed of any repeating block, summing unique invalid IDs.
- **Day 3 – Lobby (`03/solve.py`)**: Loads battery banks into a NumPy array. `sum_jolts(n)` greedily selects the next-highest digit in order to build the maximum possible `n`-digit number per bank and sums those values. Invoked for `n=2` (part 1) and `n=12` (part 2).

## Adding more days
Copy an existing day folder as a starting point, drop in the new puzzle input as `secret.input`, and implement `solve.py` to print both parts.
