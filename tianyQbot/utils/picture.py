import os
from random import choice


def get_picture(_count):
    _folder = os.path.abspath('.').replace('\\', '/')
    # print(_folder)
    with open(_folder + '/tianyQbot/src/pic.txt', 'r', encoding='utf8') as f:
        lines = f.read()
    lines = lines.split('\n')
    # print(len(lines))
    links = list()
    for i in range(int(_count)):
        links.append(choice(lines))
    # print(links)
    return links

# get_picture('5')
