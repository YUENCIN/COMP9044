#!/usr/bin/env python3
import sys
import re
big = float(-sys.maxsize)
input = []
max = 0
n = 0
max_list = []

for line in sys.stdin:

    if line == '\n':
        break
    input.append(line[:-1])
    number = str.replace(line[:-1],'--','-')
    number = re.findall(r'-?[0-9]+\.[0-9]*|-?[0-9]+', number)
    #print(number)
    for i in number:
        k = float(i)
        if k > big:
            max_list.clear()
            big = k
            max = n
            if n not in max_list:
                max_list.append(n)
        if k == big:
            big = k
            max = n
            if n not in max_list:
                max_list.append(n)
    n += 1
    #print(input,max,big,n)

for i in max_list:
    print(input[i])

