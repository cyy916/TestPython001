# -*- coding:utf-8 -*-
'''
@ File: http_request.py
@ DATE:2022/7/24
@ Author: chenyuanyuan
@ version: python 3
'''
import requests, json
from my_log import MyLogger

class HttpRequest:
    def http_request(self, method, req_url, header={}, data={}, cookie=None):
        try:
            if method.upper() == "GET":
                res = requests.get(req_url, headers=header, params=data, cookies=cookie)
            elif method.upper() == "POST":
                res = requests.post(req_url, headers=header, data=data, cookies=cookie)
            else:
                MyLogger.warning("您输入的请求方法不正确！")
            return res
        except Exception as e:
            MyLogger.error(e)
            raise e


if __name__ == "__main__":
    url = "http://www.baidu.com/"
    payload = {}
    headers = {
        'Cookie': 'BIDUPSID=51E52CCE736F469ECE498058FD92F982; PSTM=1647680536; BAIDUID=51E52CCE736F469E3E4D90770A466275:FG=1; BDSVRTM=0; BD_HOME=1; H_PS_PSSID=36552_36752_36726_36454_36413_36165_36816_36570_36746_26350_36934'
    }
    response = HttpRequest().http_request("GET", url, headers, payload)
    # MyLogger().info(response.text)
    MyLogger().info("响应头：{0}\n响应内容：{1}".format(response.headers,response.content))
