# -*- coding: utf-8 -*-
# @Time : 2023/5/22 16:12
# @Author : 23
# @Email : 2384693535@qq.com
# @File : threshold.py
# @Project : pythonProject3
# @脚本说明 :
#对404状态码进行阈值预警，相同源ip，统计404次数
#源ip通过web日志提权，访问时间正则提权，状态码正则提取
import re,time
dict={}
import csv
def open_file():
    file=open('c:/xampp/apache/logs/access.log')
    file.seek(0,2)
    while True:
        line_list=file.readlines()
        if len(line_list) >0:
            for line in line_list:
                match=re.match('(\d+\.\d+\.\d+\.\d+).+\[(.+) \+0800\].+?"(.*?)"\s+(\d+)',line)
                ip=match.group(1)
                time1=match.group(2)
                code=match.group(4)
                check(ip,time1,code)
        time.sleep(1)
def check(srcip,atime,status):
    aatime=int(time.mktime(time.strptime(atime,'%d/%b/%Y:%H:%M:%S')))
    if status=='404':
        if srcip in dict.keys():
            dict[srcip][1] = dict[srcip][1] + 1
            print(dict)
        else:
            dict[srcip]=[aatime,1]
        if dict[srcip][1]>=5:
            if aatime -dict[srcip][0]<=10:
                print(f'在连续的10秒内404超过5次源IP为{srcip}')
                dict[srcip][0]=aatime
                dict[srcip][1]=0
            else:
                dict[srcip][0]=aatime
                dict[srcip][1]=0

    # if status =='404':
    #     if srcip in dict.keys():
    #         dict[srcip]=dict[srcip]+1
    #     else:
    #         dict[srcip]=0
    # print(dict)
    # if dict[srcip]>=5:
    #     print(f'ip{srcip}访问超过5次')
    #     dict[srcip]=0
open_file()