#!/usr/bin/env python3
import math
import re
import sys
from setuptools import glob

input = sys.argv[1:]
res = {}


def get_total(name):
    sum = 0
    with open(name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            words = re.findall('[a-zA-Z]+', line)
            sum += len(words)
    return sum


def get_special(key, name):
    sum = 0
    with open(name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            words = re.findall('[a-zA-Z]+', line)
            for w in words:
                if w.upper() == key.upper():
                    sum += 1

    return sum


for file in glob.glob("lyrics/*.txt"):
    name = file[7:-4].replace('_', ' ')
    freq_list = []
    sum_log = 0
    total = get_total(file)
    for word in input:
        total_spec = get_special(word, file)
        freq_list.append((total_spec + 1)/ total)
    #print(freq_list)
    for i in freq_list:
        sum_log += math.log(i)
    #print(sum_log)
    # words = input.split(' ')
    # print(input)
    # for wor
    # s1 = get_special(key, file)
    # s2 = get_total(file)
    # cont = [s1, s2]
    res[name]=sum_log
    # freq = s1/s2
    # print(f"{s1:4}/{s2:6} = {freq:.9f} {name}")

res = sorted(res.items(), key=lambda x:x[0])
for i in res:
    name = i[0]
    value = i[1]
    print(f"{value:10.5f} {name}")
