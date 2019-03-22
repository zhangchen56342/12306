# coding:utf-8

from Api import Query
import urllib2
import ssl
import json
import sys
import re

queryApi = Query()


##############
# 查询车票
##############
def query_tickets():
    trains_ret = queryApi.query_tickets()
    trains = trains_ret['data']['result']
    for train in trains:
        train_data = train.split('|')
        for field in train_data:
            if not field:
                print '| -',
            else:
                print '| %s' % field,
        print "\n"


##############
# 查询车站
##############
def query_stations():
    stations_ret = queryApi.query_stations()  # 获取所有车站信息，拿到的结果是保存在js文件里面的一个很长的字符串
    # print stations_ret
    stations_ret = stations_ret.split("\'")[1].split("\'")[0]  # 截取两个单引号中间的字符串，就是所有的车站信息
    stations_ret_list = stations_ret.split("@")  # 每一个车站用 @ 符号隔开的，这里将它分割成列表
    if not stations_ret_list[0]:
        del stations_ret_list[0]
    # print stations_ret_list

    stations = []
    for station_info in stations_ret_list:
        station_data = station_info.split("|")
        station = {
            "char": station_data[0],  # 简拼 暂时不知道有什么用
            "name": station_data[1],  # 车站中文名
            "code": station_data[2],  # 车站代码
            "fill_name": station_data[3],  # 车站名全拼
            "char2": station_data[4],  # 简拼，暂时不知道什么用
            "num": station_data[5],  # 车站序号
        }
        print station
        del station_data
        stations.append(station)


query_stations()
# query_tickets()
