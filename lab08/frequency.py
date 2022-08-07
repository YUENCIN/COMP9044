#!/usr/bin/env python3
import re
import sys
from setuptools import glob

key = sys.argv[1]
res = {}

def get_total(name):
    sum = 0
    with open(name,'r') as f:
        lines = f.readlines()
        for line in lines:
            words = re.findall('[a-zA-Z]+', line)
            sum += len(words)
    return sum

def get_special(key, name):
    sum = 0
    with open(name,'r') as f:
        lines = f.readlines()
        for line in lines:
            words = re.findall('[a-zA-Z]+', line)
            for w in words:
                if w.upper() == key.upper():
                    sum+=1

    return sum



for file in glob.glob("lyrics/*.txt"):
    name = file[7:-4].replace('_',' ')
    s1 = get_special(key, file)
    s2 = get_total(file)
    cont = [s1, s2]
    res[name]=cont
    #freq = s1/s2
    #print(f"{s1:4}/{s2:6} = {freq:.9f} {name}")

res = sorted(res.items(), key=lambda x:x[0])
for i in res:
    name = i[0]
    s1 = i[1][0]
    s2 = i[1][1]
    freq = s1 / s2
    print(f"{s1:4}/{s2:6} = {freq:.9f} {name}")
