#!/usr/bin/env python3
import math
import re
import sys
from setuptools import glob

input = sys.argv[1:]


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


def get_log_pro(data):
    res = {}
    for file in glob.glob("lyrics/*.txt"):
        name = file[7:-4].replace('_', ' ')
        freq_list = []
        sum_log = 0
        total = get_total(file)
        for word in data:
            total_spec = get_special(word, file)
            freq_list.append((total_spec + 1) / total)
        # print(freq_list)
        for i in freq_list:
            sum_log += math.log(i)
        # cont = [s1, s2]

        res[name] = sum_log
    return res

if len(input)==5:
    for file in sorted(glob.glob("song*.txt")):
        with open(file, 'r') as f:
            res = {}
            lines = f.readlines()
            word_list = []
            lr = {}
            for line in lines:
                words = re.findall('[a-zA-Z]+', line)
                for i in words:
                    # if i not in word_list:
                    word_list.append(i)
                # print(line)
                # res = get_log_pro(line)
            res = get_log_pro(word_list)
            # print(res)
            # lr = merge_dict(res, lr)
            # print(lr)
            res = sorted(res.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
            # print(res[0])
            print('{} most resembles the work of {} (log-probability={:.1f})'.format(file, res[0][0], res[0][1]))

else:
    for file in input:
        with open(file, 'r') as f:
            res = {}
            lines = f.readlines()
            word_list = []
            lr = {}
            for line in lines:
                words = re.findall('[a-zA-Z]+', line)
                for i in words:
                    # if i not in word_list:
                    word_list.append(i)
                # print(line)
                # res = get_log_pro(line)
            res = get_log_pro(word_list)
            # print(res)
            # lr = merge_dict(res, lr)
            # print(lr)
            res = sorted(res.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
            # print(res[0])
            print('{} most resembles the work of {} (log-probability={:.1f})'.format(file, res[0][0], res[0][1]))

