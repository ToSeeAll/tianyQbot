# 基于go-cqhttp与Django实现的QQ机器人

## 食用方法：

1·  `git clone https://github.com/ToSeeAll/tianyQbot`

2·   `cd tianyQbot`

3·   `pip install -r requirements.txt`

4·   安装[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)

5·   修改go-cqhttp配置，参考`config.yml.temp` 

6·  参照`tianyQbot/src/readme.md`修改相关Django配置

7·   启动go-cqhttp，登录机器人

8·   启动Django：`cd tianyQbot根目录 ` `python manage.py 5701`

9·   请自行保持go-cqhttp与python的后台运行，可选用screen等实现进程守护
