import json
import requests


def get_pixiv_pic(_count, no_tag=None, _tag=None, _uid=None, pixiv_proxy='pic.proot.ml'):
    """
    _count,数量
    no_tag=None,排除的tag
    _tag=None,包含的tag
    _uid=None,uid
    pixiv_proxy='pic.proot.ml'，代理
    """
    # *************
    if _uid is None:
        _uid = []
    if _tag is None:
        _tag = []
    if no_tag is None:
        no_tag = ['触手', '未成年']
    # **************
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39'
    }

    data = {
        "r18": 2,
        "num": _count,
        "uid": _uid,
        "keyword": "",
        "tag": _tag,
        "size": ["original"],
        "proxy": pixiv_proxy,
        "dateAfter": "",
        "dateBefore": "",
        "dsc": "false"

    }
    url = 'https://api.lolicon.app/setu/v2'
    res = requests.post(url, headers=headers, data=json.dumps(data))
    # print(res)
    links = res.json()
    # print(links['data']['tags'])
    # print(links['data'][0]['urls']['original'])
    picture_url = list()
    for b in links['data']:
        _flag = True
        for x in no_tag:
            for tag in b['tags']:
                if x in tag:
                    _flag = False
                    break
            if not _flag:
                break
        if _flag:
            picture_url.append(b['urls']['original'])
    # print(picture_url)
    return picture_url
