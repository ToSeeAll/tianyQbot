from email import message
import json
from random import choice
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt

from tianyQbot.utils import sendMsg
from tianyQbot.utils import soutu


def chat(query, access_token, service_id):
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


@csrf_exempt
def respo(request):
    # # 加载二次元词典
    # with open(r'tianyQbot/src/data.json', 'r', encoding='utf-8') as f:
    #     data_json = f.read()
    #     # print(type(data_json))
    # dict_json = json.loads(data_json)
    with open(r'tianyQbot\src\config.json', 'r', encoding='utf-8') as f:
        config = f.read()
    config_json = json.loads(config)
    access_token = config_json['access_token']
    service_id = config_json['service_id']
    # todo 2022/5/21 设置初始化读取配置

    # ***********搜图tag
    soutuTag = False
    # todo 2022/5/21 添加另一种触发搜图的形式，可能得重构消息判断
    # ****************
    # print(dict_json.keys)
    # 接收相关
    body = request.body
    # print(body)
    data = body.decode('utf-8')
    data = json.loads(data)
    try:
        _message = data['message']
        # print(_message)
        group_id = data['group_id']
        user_id = data['user_id']
        # print(data)
    except KeyError:
        _message = ''
        group_id = ''
    try:
        if '[CQ:at,qq=2536597389]' in _message:  # 需自行把QQ改成机器人的QQ号
            # TODO：添加配置文件，实现自动配置机器人QQ以及超级用户
            if '菜单' in _message or '\xe8\x8f\x9c\xe5\x8d\x95' in _message:
                text = '目前支持功能有：\n1:以图搜图\n2.你猜我支持啥\n3.说了不支持还\n4.。。。。'
                sendMsg.send_group_msg(text, group_id)
            # elif _message.split(' ')[-1] in list(dict_json.keys()):
            #     if user_id ==429442314:#超级用户
            #         text = dict_json[_message.split(' ')[-1]]
            #         msg = choice(text)
            #     else:
            #         msg='略略略'
            #     sendMsg.send_group_msg(msg, group_id)
            elif '以图搜图' in _message:
                url = _message.split('url=')[-1].replace(']', '')
                print(url)
                if url:
                    soutu.sotu(url=url, group_id=group_id)
                else:
                    sendMsg.send_group_msg('图呢？', group_id)

            else:
                # *********自动聊天******************
                # print(_message)
                # params = {
                #     'key': 'free',
                #     'appid': '0',
                #     'msg': _message.split(' ')[-1],
                # }

                # response = requests.get(
                #     'https://api.qingyunke.com/api.php', params=params)
                # body = response.json()
                # msg = body['content'].replace('菲菲', '小丁')
                # msg = '听不懂呢'
                # print(_message)
                msg = chat((_message.split(' '))[-1], access_token, service_id)
                # print((_message.split(' '))[-1], msg)
                sendMsg.send_group_msg(msg, group_id)
    except NameError:
        pass
    return HttpResponse('返回值')
