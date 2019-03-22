# coding:UTF-8

import ssl
import urllib
import urllib2
import json
import re
import cookielib


class Query:
    __headers = {}
    __context = None

    def __init__(self):
        self.__headers = {
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Cookie": "tk=06ET5JKa10HHdHt1iCCcYAkq9Se9PdLxNkyT9pZHhMEqr1110; JSESSIONID=3E7B7DC315FF2A8C79384EAFF30FAB5D; RAIL_EXPIRATION=1496523643264; RAIL_DEVICEID=UQrKk7a1-pE25_Y_SpjdPzRjvna5INJbd0OHdy-o-NnnaTRSRhMzM6TKmXOzzxINauwl8O53CgRUXaGuAotCOQRoEjcki86n9A08qFhilK8d10umGjGd1V9Y7RyvK6--CB9KYCTFsNhQGiwz5cO7RmLa0JMHEIyE; RAIL_OkLJUJ=FDbBvEme1XzKRDpHE2zLiSEb23c0u8Nl; route=c5c62a339e7744272a54643b3be5bf64; BIGipServerotn=2179465482.64545.0000; BIGipServerportal=3084124426.17695.0000; BIGipServerpassport=937951498.50215.0000; _jc_save_detail=true; current_captcha_type=Z; _jc_save_fromStation=%u5E7F%u5DDE%2CGZQ; _jc_save_toStation=%u6F6E%u9633%2CCNQ; _jc_save_fromDate=2017-07-25; _jc_save_toDate=2017-07-24; _jc_save_wfdc_flag=dc",
            "Host": "kyfw.12306.cn",
            "If-Modified-Since": "0",
            "Referer": "https://kyfw.12306.cn/otn/leftTicket/init",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
            "Content-Type": "charset=UTF-8"
        }
        self.__context = ssl._create_unverified_context()

    #########################
    # 查询所有站点的名称和字母代码
    #########################
    def query_stations(self):
        url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9019"
        res = self.get_response(url)
        return res

    ###########################
    # 查询车票
    ###########################
    def query_tickets(self):
        url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-07-26&leftTicketDTO.from_station=GZQ&leftTicketDTO.to_station=CNQ&purpose_codes=ADULT"
        res = self.get_response(url)
        return res

    ####################################################
    # 请求访问接口，拿到返回数据（这是一个类方法）
    # 普通方法,可以通过self访问实例属性，类方法,可以通过cls访问类属性，静态方法,不可以访问,通过传值的方式
    ####################################################
    def get_response(self, url, data=None, req_type="form"):  # form/json
        req = urllib2.Request(url=url)  # 默认get方法，

        # 如果data不为空，根据请求类型，对data格式进行转换，并且添加相应的header头
        if data:
            req_data = urllib.urlencode(data)
            if req_type == "json":
                req_data = json.dumps(data)
                content_type = "application/json"
                self.__headers["content-type"] = content_type
            req = urllib2.Request(url=url, data=req_data)

        response = urllib2.urlopen(req, context=self.__context)
        result = response.read()
        return self.__get_json(result)

    ####################
    # 讲json数据转换为dict
    ####################
    @staticmethod
    def __get_json(data):
        try:
            data = json.loads(data)
        except ValueError:
            return data
        return data
