#!/usr/bin/python3
import sys
try:
    chess = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
try:
    if len(sys.argv) != 2:
        raise TypeError("Usage: nqueens N")
    if chess < 4:
        raise TypeError("N must be at least 4")
except (TypeError, ValueError) as err:
    print(err)
    exit(1)
for tried in range(chess):
    pos = [[a, b] for a in range(chess) for b in range(chess)]
    for attemp in
print(pos)
