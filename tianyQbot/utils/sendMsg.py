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


def send_group_pic(pictures, group_id, auto_escape='false'):
    header = {
        'Content-Type': 'application/json'
    }
    url = 'http://127.0.0.1:5700/send_group_msg'
    _messages = ''
    print(type(pictures))
    if isinstance(pictures, list):
        for x in pictures:
            _messages += '[CQ:image,file=' + x + ']'
    elif isinstance(pictures, str):
        _messages = pictures
    print(_messages)
    data = {
        'group_id': str(group_id),
        'message': _messages,
        'auto_escape': auto_escape
    }
    message = json.dumps(data)
    # print(message)
    res = requests.post(url, headers=header, data=message)
    # print(res.text)
    return res
