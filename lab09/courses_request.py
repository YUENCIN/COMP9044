#!/usr/bin/env python3
import requests
import re
import sys



if len(sys.argv) == 2:
    prefix = sys.argv[1]
    url = 'http://timetable.unsw.edu.au/2022/'+prefix+'KENS.html'
    resp = requests.get(url)
    html = str(resp.content, encoding='utf-8')
    content = "<td class=\"data\"><a href=\""+prefix+'.*'
    res = re.findall(content,html)
    record = []
    for i in res:
        record.append(i[41:-9])

    n = len(record)
    for i in range(0,n):
        if i % 2 == 0:
            print(record[i],record[i+1])
