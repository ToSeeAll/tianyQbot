from email import message
import json
from random import choice
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt

from tianyQbot.utils import sendMsg


@csrf_exempt
def respo(request):
    # 加载二次元词典
    with open(r'tianyQbot/src/data.json', 'r', encoding='utf-8') as f:
        data_json = f.read()
        # print(type(data_json))
    dict_json = json.loads(data_json)
    # print(dict_json.keys)
    # 接收相关
    body = request.body
    # print(body)
    data = body.decode('utf-8')
    data = json.loads(data)
    try:
        message = data['message']
        # print(message)
        group_id = data['group_id']
        user_id = data['user_id']
        # print(data)
    except KeyError:
        pass
    try:
        if '[CQ:at,qq=2536597389]' in message:#需自行把QQ改成机器人的QQ号
            #TODO：添加配置文件，实现自动配置机器人QQ以及超级用户
            if '菜单' in message or '\xe8\x8f\x9c\xe5\x8d\x95' in message:
                text = '目前支持功能有：\n1:啥都不支持\n2.你猜我支持啥\n3.说了不支持还\n4.。。。。'
                sendMsg.send_group_msg(text, group_id)
            elif message.split(' ')[-1] in list(dict_json.keys()):
                if user_id ==429442314:#超级用户
                    text = dict_json[message.split(' ')[-1]]
                    msg = choice(text)
                else:
                    msg='略略略'
                sendMsg.send_group_msg(msg, group_id)
            else:
                # *********自动聊天******************
                # print(message)
                # params = {
                #     'key': 'free',
                #     'appid': '0',
                #     'msg': message.split(' ')[-1],
                # }

                # response = requests.get(
                #     'https://api.qingyunke.com/api.php', params=params)
                # body = response.json()
                # msg = body['content'].replace('菲菲', '小丁')
                msg = '听不懂呢'
                sendMsg.send_group_msg(msg, group_id)
    except NameError:
        pass
    return HttpResponse('返回值')
