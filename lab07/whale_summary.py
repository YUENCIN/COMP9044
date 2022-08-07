#!/usr/bin/env python3
import sys

def process(name):
    res = name
    new = ''
    if name[-1]=='s':
        res = name[:-1]
    ls = res.split(" ")
    for k in ls:
        if k!="":
            #print(k)
            new+=k
            new+=' '
    #print(new[:-1])
    return new[:-1]

sum = 0
dict_pod = {}
dict_ind = {}
name_list = []
n = len(sys.argv)

if n >= 2:
    for i in range(1, n):
        file_name = sys.argv[i]
        with open(file_name, 'r') as f:
            lines = f.readlines()
            for line in lines:
                name = line[12:-1].lower()
                name = process(name)
                # print(name)
                ind = int(line[9:11])
                if name not in name_list:
                    name_list.append(name)
                if name not in dict_ind.keys():
                    dict_ind[name] = 0
                if name not in dict_pod.keys():
                    dict_pod[name] = 0

                dict_ind[name] += ind
                dict_pod[name] += 1

name_list.sort()
for name in name_list:
    print(name+" observations: "+str(dict_pod[name])+" pods, "+str(dict_ind[name])+" individuals")
