import json

import requests


def baidu_chat(query, access_token, service_id):
    """
    query >> 请求文本
    access_token >> 机器人的access_token
    service_id >> 机器人id
    """
    url = 'https://aip.baidubce.com/rpc/2.0/unit/service/v3/chat?access_token=' + access_token
    post_data = {
        "version": "3.0",
        "service_id": service_id,
        "session_id": "",
        "log_id": "7758521",
        "request": {
            "terminal_id": "88888",
            "query": query
        }
    }
    post_data = json.dumps(post_data)
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, data=post_data, headers=headers)
    if response:
        # print(response.json())
        return response.json()['result']['context']['SYS_PRESUMED_HIST'][-1]
    else:
        return '调用接口失败，请检查access_token是否过期或者其它错误'
