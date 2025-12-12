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
- **Day 8 – Playground (`08/solve.py`)**: Coordinate clustering using pairwise distances. Part 1 finds the 1000 closest coordinate pairs, merges them into clusters, and returns the product of the three largest cluster sizes. Part 2 continues merging until all coordinates form a single cluster and multiplies the x-coordinates of the final merged pair.
- **Day 9 – Movie Theater (`09/solve.py`)**: Rectangular area calculation from coordinate vertices. Part 1 finds the maximum rectangular area between any two coordinates. Part 2 finds the maximum area that doesn't intersect any line segments formed by consecutive coordinate pairs in the polygon loop.
- **Day 10 – Factory (`10/solve.py`)**: Binary light puzzle with XOR button operations. Lights are represented as binary numbers, and buttons toggle specific bit patterns. Part 1 finds the minimum number of button presses needed to turn off all lights by testing power set combinations.
- **Day 11 – Reactor (`11/solve.py`)**: Graph path counting in a directed graph parsed from adjacency lists. Part 1 counts all paths from node 'you' to 'out'. Part 2 counts paths from 'svr' to 'out' while blocking specific nodes ('dac' and 'fft').
- **Day 12 – Christmas Tree Farm (`12/solve.py`)**: Tree shape fitting with degrees of freedom calculation. Parses shape templates and tree specifications (dimensions and piece counts). Part 1 filters trees that have non-negative degrees of freedom based on available pieces. Part 2 is locked pending completion of other puzzles.

## Requirements

- Python 3.11+ (tested locally)
- `numpy` (`pip install numpy`)

