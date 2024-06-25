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
lis = []
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
                                url=match.group(2)

                                code = match.group(4)
                                result=access_rules('accesslog.csv')
                                if re.search('404', code,re.IGNORECASE):  # 匹配状态码
                                    print('可能存在扫描')
                                    print(f'原日志{line}')
                                    time_match(ip)
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
                            elif decoder1['logname']=='errlog':
                                ip=match.group(1)
                                url=match.group(2)
                                result=access_rules('errorlog.csv')
                                for rule in result: #取出规则的正则表达式
                                    rul=rule['rul']
                                    if re.search(rul,url,re.IGNORECASE):#匹配规则库
                                        print(rule['name'])
                                        print(f'原日志{line}')
            time.sleep(5)
        except:
            file.close()


def time_match(ip):
        # 为每个IP地址创建一个新的字典，用于储存请求时间
        ip_request_time = {}
        start_time = datetime.datetime.now()
        ip_request_time[ip] = start_time
        lis.append(ip_request_time)
        if count_ip(ip) >= 10:
            time1 = (datetime.datetime.now() - get_ip_time(ip)).total_seconds()

            if time1 < 10:
                print(f"发送大量404请求进行IP封禁，IP地址为{ip}")
                ip_filrewalld(ip)
                lis.clear()
            else:
                lis.clear()
def count_ip(ip):
    count1 = 0
    for request_time in lis:
        if ip in request_time:
            count1 += 1
    return count1
def get_ip_time(ip):
    for request_time in lis:
        if ip in request_time:
            return request_time[ip]
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
    code = os.system(f"firewall-cmd  --add-rich-rule='rule family=\"ipv4\" source address=\"{ip}\" service name=\"http\" reject ' --timeout=60s ")
    if code == 0:
        print('成功')
with open('data.csv','r')as fp:
    logs=fp.readlines()
for log in logs:
    log=log.strip()
    th=threading.Thread(target=read_file,args=(log,))
    th.start()
th.join()