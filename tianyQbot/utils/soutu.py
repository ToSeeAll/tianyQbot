import json

import requests
from urllib3.exceptions import RequestError

from tianyQbot.utils import sendMsg


def __format_send(a, group_id):
    results = a['results']
    res = list()
    for i in range(3):
        r = dict()
        k = results[i]
        r['similarity'] = k['header']['similarity']
        r['data'] = k['data']
        res.append(r)
    # print(res)
    for i in range(min(3, len(res))):
        re = res[i]
        _sotu = '相似度:' + str(re['similarity']) + '\n' + json.dumps(re['data'], ensure_ascii=False).replace('{',
                                                                                                           '').replace(
            '}',
            '').replace(
            ',',
            '\n').replace(
            '"', '') + '\n'
        sendMsg.send_group_msg(_sotu, group_id)


def sotu(url, group_id):
    with open(r'tianyQbot\src\config.json', 'r', encoding='utf-8') as f:
        config = f.read()
    config_json = json.loads(config)
    URL = "https://saucenao.com/search.php"
    params = dict()
    params["api_key"] = config_json['sotu_api_key']  # api_key
    # todo 2022/5/21 初始化函数，把这些参数放进去
    params["output_type"] = 2
    params["testmode"] = 1
    params["dbmaski"] = 32768
    params["db"] = 5
    params["numres"] = 5
    params[  # 待搜索图片
        "url"] = url
    try:
        res = requests.get(URL, params=params)
    except RequestError:
        res = {"Request failed!": ""}
    data = res.json()
    __format_send(data, group_id)
