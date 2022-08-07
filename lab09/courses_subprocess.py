#!/usr/bin/env python3
import re
import subprocess
import sys

if len(sys.argv) == 2:
    prefix = sys.argv[1]
    url = 'http://timetable.unsw.edu.au/2022/'+prefix+'KENS.html'
    cmd_list = ['curl']
    cmd_list.append(url)
    out = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()
    html = str(stdout, encoding='utf-8')
    content = "<td class=\"data\"><a href=\""+prefix+'.*'
    res = re.findall(content,html)
    record = []
    for i in res:
        record.append(i[41:-9])

    n = len(record)
    for i in range(0,n):
        if i % 2 == 0:
            print(record[i],record[i+1])
