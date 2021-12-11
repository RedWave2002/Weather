# -*- coding = utf-8 -*-
# @Time : 2021/10/4 11:26
# @Author : Ram
# @File : Weather.py
# @Software : PyCharm

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re                      # 正则表达式，进行文字匹配
import urllib.request          # 指定url，获取网页数据
import urllib.error            # urllib error
import requests


def main():
    yc_url = "http://www.weather.com.cn/weather1d/101200901.shtml"
    wh_url = "http://www.weather.com.cn/weather1d/101200101.shtml"
    yc = get_data(yc_url)
    wh = get_data(wh_url)
    data_yc = manage_str(yc)
    data_wh = manage_str(wh)
    qq1 = "794935952"
    # qq2 = "1961456079"

    send_msg(data_yc, data_wh, qq1)
    # send_msg(data_yc, data_wh, qq2)


def get_data(url):
    head = {
        "User-Agent": "Mozilla/5.0 = Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    }
    req = urllib.request.Request(url, headers = head)
    html = ""
    try:
        res = urllib.request.urlopen(req)
        html = res.read().decode('UTF-8')

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    soup = BeautifulSoup(html, "html.parser")
    data = soup.find_all(id = "hidden_title")
    data = str(data)
    find_wea = re.compile(r'<input id="hidden_title" type="hidden" value="(.*?)">')
    weather = re.findall(find_wea, data)[0]
    return weather


def send_msg(msg1, msg2, qq):
    m = "早上好呀~" + '\n' + "现在是" + msg1[0] + ' ' + msg1[1] + '\n' + "今日天气：" + '\n' + "宜昌 " + msg1[2] + '\n' + "武汉 " + msg2[2]
    KEY = '0a5ba7b9077b55eb38ccad4c70730c3d'
    data = {
        "msg": m,           # 需要发送的消息
        "qq": qq            # 需要接收消息的QQ号码
    }
    url = 'https://qmsg.zendee.cn/group/' + KEY    # 群消息推送接口
    # url2 = 'https://qmsg.zendee.cn/send/' + KEY  # 私聊消息推送接口

    response = requests.post(url, data = data)
    # response = requests.post(url2, data = data)

def manage_str(str):
    data = []
    f_date = re.compile(r'.*?月.*?日.*?时')
    f_week = re.compile(r'周.')
    date = re.findall(f_date, str)[0]
    week = re.findall(f_week, str)[0]
    weather = str[len(date) + len(week) + 3:]
    data.append(date)
    data.append(week)
    data.append(weather)
    return data

if __name__ == "__main__":
    main()
