#!/usr/bin/env python3
import sys
import re

sum = 0
n = len(sys.argv)
if n == 2:
    file_name = sys.argv[1]
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            for word in line[:-1].split(" "):
                number = re.findall(r"[0-9]+", word)
                if number:
                    for k in number:
                        a = float(k)
                        b = int(a)
                        sum += b
                # if word.isdigit():
                # sum += int(word)

print(sum)
