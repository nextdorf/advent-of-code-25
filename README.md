# Advent of Code 2025

Python solutions for Advent of Code 2025 puzzles. Each day lives in its own folder with the problem statement, my input, and a solver script that prints both puzzle answers.

## Setup

Each day folder requires a `secret.input` file containing your personal puzzle input. **Important:** The input file must not have trailing empty lines.

## Running a day

From the repo root:

```bash
python <DAY>/solve.py
```

## Solution notes

- **Day 1 – Secret Entrance (`01/solve.py`)**: Parses dial rotations and uses cumulative sums mod 100 to count times the dial lands on 0 (part 1). Part 2 walks each rotation to count every intermediate click that crosses 0.
- **Day 2 – Gift Shop (`02/solve.py`)**: Reads comma-separated ID ranges. Part 1 filters even-length numbers that are exactly two repeated halves. Part 2 precomputes divisors for each possible digit length and checks whether a number is composed of any repeating block, summing unique invalid IDs.
- **Day 3 – Lobby (`03/solve.py`)**: Loads battery banks into a NumPy array. `sum_jolts(n)` greedily selects the next-highest digit in order to build the maximum possible `n`-digit number per bank and sums those values. Invoked for `n=2` (part 1) and `n=12` (part 2).
- **Day 4 – Printing Department (`04/solve.py`)**: Grid-based forklift counting. Part 1 counts `@` symbols with fewer than 4 adjacent forklifts. Part 2 iteratively removes undercrowded forklifts until no more can be removed, tracking the total count.
- **Day 5 – Cafeteria (`05/solve.py`)**: ID range validation. Part 1 counts how many available IDs fall within any given range. Part 2 merges overlapping ranges and calculates the total count of unique IDs across all merged ranges.
- **Day 6 – Trash Compactor (`06/solve.py`)**: Numeric grid operations with operators. Part 1 applies column-wise operations (sum or product) based on a sequence of operators. Part 2 reads vertically-aligned numbers separated by spaces and applies operators to each group.
- **Day 7 – Laboratories (`07/solve.py`)**: Beam propagation simulation through a grid. Starts from position 'S' and traces a beam downward. When hitting '^' symbols, the beam splits left and right. Part 1 counts total collisions with '^' obstacles. Part 2 counts all positions reached by the beam after full propagation.

## Requirements

- Python 3.11+ (tested locally)
- `numpy` (`pip install numpy`)

