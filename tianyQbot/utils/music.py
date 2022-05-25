import asyncio
import httpx


async def search_163(keyword: str):
    url = "https://music.163.com/api/cloudsearch/pc"
    params = {"s": keyword, "type": 1, "offset": 0, "limit": 1}
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, params=params)
        result = resp.json()
    if songs := result["result"]["songs"]:
        return songs
    return "网易云音乐中找不到相关的歌曲"


def music_163(_word):
    song = asyncio.run(search_163(_word))
    # print(song[0]['id'])
    music = '[CQ:music,type=163,id=' + str(song[0]['id']) + ']'
    return music
