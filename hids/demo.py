import re
import csv
import datetime
import time
dict= {}

def time_match(ip):
    start_time = datetime.datetime.now()
    if ip  in dict.keys():
        dict[ip][1] = dict[ip][1] + 1
    else:
        dict[ip]=[start_time,1]
    if dict[ip][1] >= 5:
        if (start_time - dict[ip][0]).total_seconds() <= 10:
            print(f'在连续的10秒内爆破数据库超过5次源IP为{ip}')
            dict[ip][0] = start_time
            dict[ip][1] = 0
        else:
            dict[ip][0] = start_time
            dict[ip][1] = 0
