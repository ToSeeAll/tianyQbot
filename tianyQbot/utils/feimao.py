import requests


def direct_link(code):
    # code = 'he0e3znm'  # 飞猫云的识别码，一般为8位
    fm_url = 'https://www.feimaoyun.com/s/' + code
    api_url = 'http://api.ilzya.com:1306/resolve'  # 作者的服务器，可能会ji
    data = {
        "url": fm_url  # 必须这个格式才行，不然接口不识别
    }
    res = requests.post(api_url, data=data)
    json_info = res.json()
    print(json_info, code)
    if json_info['message'] == '解析成功':
        return json_info['durl']  # 下载链接
    else:
        return json_info['message']
