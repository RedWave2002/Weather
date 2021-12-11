# -*- coding = utf-8 -*-
# @Time : 2021/12/11 13:21
# @Author : Ram
# @File : test.py
# @Software : PyCharm
import requests

def main():
    m = "早上好"
    KEY = 'ada531e9a634fca7aebb4efa873d0ad4'
    data = {
        "msg": m,           # 需要发送的消息
        "qq": "1961456079"  # 需要接收消息的QQ号码
    }
    # url = 'https://qmsg.zendee.cn/group/' + KEY    # 群消息推送接口
    url2 = 'https://qmsg.zendee.cn/send/' + KEY    # 私聊消息推送接口

    # response = requests.post(url, data = data, timeout = 5)
    response = requests.post(url2, data = data)

if __name__ == "__main__":
    main()
