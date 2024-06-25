# -*- coding: utf-8 -*-
# @Time : 2023/5/20 11:16
# @Author : 23
# @Email : 2384693535@qq.com
# @File : readlog.py
# @Project : pythonProject3
# @脚本说明 :
import threading
import time
import re
import csv
import datetime
import os
dict1={}
dict2={}
def read_file(data):
    file = open(rf'{data}')
    file.seek(0, 2) # 直接定位到文件末尾
    print(f"================ 开始实时读取{data}日志信息 ================")
    while True:
        try:
            list = file.readlines()        # 每一次均读取最新内容，此处并不需要使用f.tell()，因为readlines会读取到最后位置
            if len(list) > 0:
                for line in list:
                    decoders=decoder_rules()
                    for decoder1 in decoders:
                        pattern =decoder1['decoder']  #取出解码器的正则表达式
                        match = re.search(pattern, line)
                        if match:  #如果匹配到判断解码器日志名 走不同分支
                            if decoder1['logname']=='access':
                                ip=match.group(1)
                                time1=match.group(2)
                                url=match.group(3)
                                code = match.group(4)
                                result=access_rules('accesslog.csv')
                                if code == '404':
                                    print('可能存在扫描')
                                    print(f'原日志{line}')
                                    check(ip,time1)
                                for rule in result: #取出规则的正则表达式
                                    rul=rule['rul']
                                    if re.search(rul,url,re.IGNORECASE):#匹配规则库
                                        print(rule['name'])
                                        print(f'原日志{line}')
                            elif decoder1['logname']=='mysql':
                                sql=match.group(1)
                                if re.search('updatexml|load_file|database|into.*outfile|extractvalue|floor|geometrycollection|multipoint|polygon|multipolygon|linestring|multilinestring|exp',sql,re.IGNORECASE):
                                    print('存在敏感操作')
                                    print(f'原日志{line}')
                            elif decoder1['logname'] == 'mysqlcoonct':
                                print('mysql登录失败')
                                print(f'原日志{line}')
                                ip=match.group(1)
                                time_match(ip)
            time.sleep(1)
        except:
            file.close()


def check(srcip,atime):
    aatime=int(time.mktime(time.strptime(atime,'%d/%b/%Y:%H:%M:%S')))
    if srcip in dict1.keys():
        dict1[srcip][1] = dict1[srcip][1] + 1
    else:
        dict1[srcip]=[aatime,1]
    if dict1[srcip][1]>=5:
        if aatime -dict1[srcip][0]<=10:
            print(f'在连续的10秒内404超过5次源IP为{srcip}')
            dict1[srcip][0]=aatime
            dict1[srcip][1] = 0
            ip_filrewalld(srcip)
        else:
            dict1[srcip][0]=aatime
            dict1[srcip][1]=0
def time_match(ip):
    start_time = datetime.datetime.now()
    if ip  in dict2.keys():
        dict2[ip][1] = dict2[ip][1] + 1
    else:
        dict2[ip]=[start_time,1]
    if dict2[ip][1] >= 5:
        if (start_time - dict2[ip][0]).total_seconds() <= 10:
            print(f'在连续的10秒内爆破数据库超过5次源IP为{ip}')
            dict2[ip][0] = start_time
            dict2[ip][1] = 0
        else:
            dict2[ip][0] = start_time
            dict2[ip][1] = 0
# def time_match(ip):
#         # 为每个IP地址创建一个新的字典，用于储存请求时间
#         ip_request_time = {}
#         start_time = datetime.datetime.now()
#         ip_request_time[ip] = start_time
#         lis.append(ip_request_time)
#         if count_ip(ip) >= 10:
#             time1 = (datetime.datetime.now() - get_ip_time(ip)).total_seconds()
#
#             if time1 < 10:
#                 print(f"发送大量404请求进行IP封禁，IP地址为{ip}")
#                 ip_filrewalld(ip)
#                 lis.clear()
#             else:
#                 lis.clear()
# def count_ip(ip):
#     count1 = 0
#     for request_time in lis:
#         if ip in request_time:
#             count1 += 1
#     return count1
# def get_ip_time(ip):
#     for request_time in lis:
#         if ip in request_time:
#             return request_time[ip]
def access_rules(path):     #读入access日志的规则库并把读取的值变为字典类型，方便取值
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # 获取文件的首行作为字典的键
        result = []
        for row in reader:
            d = dict(zip(headers, row))  # 将每行数据与键合并为字典
            result.append(d)
        return result
def decoder_rules():    #读取解码器的规则库并把读取的值变为字典类型，方便取值
    with open('decoder.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # 获取文件的首行作为字典的键
        decode = []
        for row in reader:
            d = dict(zip(headers, row))  # 将每行数据与键合并为字典
            decode.append(d)
        return decode
def ip_filrewalld(ip):
    code = os.system(f'netsh advfirewall firewall add rule name="http" dir=in action=block protocol=tcp remoteip={ip} localport=80')
    if code == 0:
        print('成功')
with open('data.csv','r')as fp:
    logs=fp.readlines()
for log in logs:
    log=log.strip()
    th=threading.Thread(target=read_file,args=(log,))
    th.start()
th.join()