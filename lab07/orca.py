#!/usr/bin/env python3
import sys

sum = 0
n = len(sys.argv)
if n >= 2:
    for i in range(1, n):
        file_name = sys.argv[i]
        with open(file_name, 'r') as f:
            lines = f.readlines()
            for line in lines:
                k = line[12:-1]
                if k == 'Orca':
                    sum += int(line[9:11])

print(str(sum) + ' Orcas reported')
