#! /usr/bin/env python3
from operator import itemgetter
import sys
current_item=None
current_count = 0
item = None
for line in sys.stdin:
    line.strip()
    try :
        item,count = line.split('\t')
        count = int(count)
    except ValueError:
        continue
    if current_item == item:
        current_count +=count
    else:
        if current_item:
            print(current_item,"\t",current_count)
        current_item =item
        current_count = count
if current_item == item:
    print(current_item,"\t",current_count)
