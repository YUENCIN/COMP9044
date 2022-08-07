#!/usr/bin/env python3
import sys
seen = {}
if len(sys.argv) == 2:
    nth = int(sys.argv[1])
    for line in sys.stdin:
        if line == '\n':
            break
        input = line[:-1]
        if input not in seen.keys():
            seen[input] = 0
        seen[input] += 1
        if seen[input] == nth:
            print("Snap:", input)
            break

