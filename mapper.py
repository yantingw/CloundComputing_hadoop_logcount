#! /usr/bin/env python3
import sys
for line in sys.stdin:
    _time = line.split('[')[1].split(']')[0]
    times  =_time.split(':')
    day = times[0]
    hour=times[1]
    key = day+ ':'+ hour +':xx:xx'
    print(key,'\t',1)
