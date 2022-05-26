import json
import os

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from tianyQbot.models import Config
from tianyQbot.utils import sendMsg, feimao, tts, picture, setu, music, soutu, chat, minecraft

# *************读取配置文件*****
with open(r'tianyQbot/src/config.json', 'r', encoding='utf-8') as f:
    config = f.read()
config_json = json.loads(config)
access_token = config_json['access_token']
service_id = config_json['service_id']
QQ_bot_id = config_json['QQ_bot_id']
no_tag = config_json['no_tag']
pixiv_proxy = config_json['pixiv_proxy']


# todo 2022/5/21 设置初始化读取配置

# ****************************


@csrf_exempt
def respo(request):
    # # 加载二次元词典
    # with open(r'tianyQbot/src/data.json', 'r', encoding='utf-8') as f:
    #     data_json = f.read()
    #     # print(type(data_json))
    # dict_json = json.loads(data_json)

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
        if '[CQ:at,qq=' + QQ_bot_id + ']' in _message:  # 需自行把QQ改成机器人的QQ号
            # *************菜单*******************
            if '菜单' in _message or '\xe8\x8f\x9c\xe5\x8d\x95' in _message:
                text = '目前支持功能有：\n0.帮助\n1:以图搜图\n2.飞猫云解析\n3.语音转文本\n4.妹子图\n5.二次元\n6.音乐（确信）\n7.不到啊'
                sendMsg.send_group_msg(text, group_id)
            # elif _message.split(' ')[-1] in list(dict_json.keys()):
            #     if user_id ==429442314:#超级用户
            #         text = dict_json[_message.split(' ')[-1]]
            #         msg = choice(text)
            #     else:
            #         msg='略略略'
            #     sendMsg.send_group_msg(msg, group_id)
            # *************以图搜图*******************
            elif '帮助' in _message:
                text = '帮锤子，自己探索'
                sendMsg.send_group_msg(text, group_id)
            elif '以图搜图' in _message:
                url = _message.split('url=')[-1].replace(']', '')
                # print(url)
                if url:
                    soutu.sotu(url=url, group_id=group_id)
                else:
                    sendMsg.send_group_msg('图呢？', group_id)
            # *************飞猫云直链解析*******************
            elif '飞猫' in _message:
                _code = _message.split(' ')[-1]
                if len(_code) == 8:
                    _directLink = feimao.direct_link(_code)
                    sendMsg.send_group_msg(_directLink, group_id)
                else:
                    sendMsg.send_group_msg("请检查格式：【飞猫 8位飞猫云识别码】|【飞猫云 8位识别码】", group_id)
            # *************自动聊天*******************
            elif '语音' in _message:
                _text = _message.split(' ')[-1]
                if tts.text2mp3(_text):
                    _folder = os.path.abspath('.').replace('\\', '/')
                    sendMsg.send_group_msg('[CQ:record,file=file:///' + _folder + '/tianyQbot/src/output.mp3]',
                                           group_id)
                else:
                    sendMsg.send_group_msg('转换失败', group_id)
            elif '图片' in _message:
                if '黑丝' in _message:
                    _count = _message.split(' ')[-1]
                    pictures = picture.get_picture_heisi(_count)
                else:
                    _count = _message.split(' ')[-1]
                    pictures = picture.get_picture(_count)
                # print(pictures)
                sendMsg.send_group_pic(pictures, group_id)
            elif '二刺螈' in _message:
                _count = _message.split(' ')[-1]
                pictures = setu.get_pixiv_pic(_count, no_tag)
                # print(pictures)
                sendMsg.send_group_pic(pictures, group_id)
            elif '音乐' in _message:
                if '网易' in _message:
                    _word = _message.split(' ')[-1]
                    _music = music.music_163(_word)
                    sendMsg.send_group_msg(_music, group_id)
                elif 'QQ' in _message:
                    # print(_message)
                    _word = _message.split(' ')[-1]
                    _music = music.music_qq(_word)
                    sendMsg.send_group_msg(_music, group_id)
            #     elif '普通' in _message:
            #         sendMsg.send_group_msg(
            #             '[CQ:music,type=custom,url=https://gitee.com/toseeall/JSP_Exce/raw/master/src/main/webapp/Ch4/music/4.mp3,audio=https://gitee.com/toseeall/JSP_Exce/raw/master/src/main/webapp/Ch4/music/4.mp3,title=音乐标题]', group_id)
            elif '数据库' in _message:
                d = dict(qq='2387581631', sex='男')
                c = Config.objects.using('user').create(**d)
                print(c.__dict__)
                sendMsg.send_group_msg('执行完毕', group_id)
            elif 'mc' or '我的世界' in _message:
                if '坐标' in _message:
                    _x = _message.split(' ')[-2]
                    _z = _message.split(' ')[-1]
                    if '地狱' in _message:
                        _new_x, _new_z = minecraft.coordinates(_x, _z, False)
                    else:
                        _new_x, _new_z = minecraft.coordinates(_x, _z, True)
                    _text = 'X: ' + str(int(_new_x)) + ' Z:' + str(int(_new_z))
                    sendMsg.send_group_msg(_text, group_id)
            else:
                # *********自动聊天******************
                # print(_message)
                msg = chat.baidu_chat((_message.split(' '))[-1], access_token, service_id)
                # print((_message.split(' '))[-1], msg)
                sendMsg.send_group_msg(msg, group_id)
    except NameError:
        pass
    return HttpResponse('返回值')
