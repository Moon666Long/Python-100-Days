# 人生苦短，我学Python
# 2021年10月14日
'''from random import randint, sample

def generate():
    """生成一组随机号码"""

    red_balls = [x for x in range(1, 34)]
    selected_balls = sample(red_balls, 6)

    selected_balls.sort()

    selected_balls.append(randint(1, 16))
    return selected_balls



def display(balls):
    """输出一组双色球号码"""
    for index, ball in enumerate(balls):
        print(f'{ball:0>3d}', end=' ')
        if index == len(balls) - 2:
            print('|', end=' ')
    print()

num = int(input('机选几注: '))
for _ in range(num):
    display(generate())'''
import random
import time

import requests
from bs4 import BeautifulSoup

for page in range(10):
    resp = requests.get(
        url=f'https://movie.douban.com/top250?start={25 * page}',
        headers={'User-Agent': 'BaiduSpider'}
    )
    soup = BeautifulSoup(resp.text, "lxml")
    for elem in soup.select('a > span.title:nth-child(1)'):
        print(elem.text)
    time.sleep(random.random() * 5)