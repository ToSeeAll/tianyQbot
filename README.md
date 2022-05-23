# 基于go-cqhttp与Django实现的QQ机器人

## 食用方法：

1·  `git clone https://github.com/ToSeeAll/tianyQbot`

2·   `cd tianyQbot`

3·   `pip install -r requirements.txt`

4· 安装[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)

5· 修改go-cqhttp配置，参考`config.yml.temp`

6· 参照`tianyQbot/src/readme.md`修改相关Django配置

7· 启动go-cqhttp，登录机器人

8· 启动Django：`cd tianyQbot根目录 ` `python manage.py 5701`

9· 请自行保持go-cqhttp与python的后台运行，可选用screen等实现进程守护

#### Tips:

语音功能需ffmpeg支持，请自行配置，可参考[ffmpeg](https://docs.go-cqhttp.org/guide/quick_start.html#%E5%AE%89%E8%A3%85-ffmpeg)

!不理解命令 请勿使用管理员权限执行设置环境变量的命令，不听老人言，吃亏在眼前。