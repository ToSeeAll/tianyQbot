import asyncio
import httpx


async def __search_163(keyword: str):
    url = "https://music.163.com/api/cloudsearch/pc"
    params = {"s": keyword, "type": 1, "offset": 0, "limit": 1}
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, params=params)
        result = resp.json()
    if songs := result["result"]["songs"]:
        return songs
    return "网易云音乐中找不到相关的歌曲"


async def __search_qq(keyword: str):
    url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp"
    params = {"p": 1, "n": 1, "w": keyword, "format": "json"}
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)
        result = resp.json()
    if songs := result["data"]["song"]["list"]:
        return songs
    return "QQ音乐中找不到相关的歌曲"


def music_163(_word):
    song = asyncio.run(__search_163(_word))
    # print(song[0]['id'])
    music = '[CQ:music,type=163,id=' + str(song[0]['id']) + ']'
    return music


def music_qq(_word):
    song = asyncio.run((__search_qq(_word)))
    music = '[CQ:music,type=qq,id=' + str(song[0]["songid"]) + ']'
    return music
