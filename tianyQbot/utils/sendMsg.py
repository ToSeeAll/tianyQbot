import json

import requests


def send_msg():
    pass


def send_group_msg(text, group_id, auto_escape='false'):
    header = {
        'Content-Type': 'application/json'
    }
    url = 'http://127.0.0.1:5700/send_group_msg'
    data = {
        'group_id': str(group_id),
        'message': text,
        'auto_escape': auto_escape
    }
    message = json.dumps(data)
    # print(message)
    res = requests.post(url, headers=header, data=message)
    # print(res.text)
    return res
