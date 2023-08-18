from random import random, randint

import requests
import ProxyPool
from faker import Faker
from tqdm import tqdm

# 目标域名
target_url = 'https://ywenrou.cn'


def generate_random_headers():
    fake = Faker()

    headers = {
        'Accept': fake.mime_type(),
        'Accept-Encoding': fake.random_element(elements=('gzip', 'deflate', 'br')),
        'Accept-Language': fake.language_code(),
        'Cache-Control': 'max-age=' + str(randint(0, 3600)),
        'Cookie': fake.password(length=20),
        'If-Modified-Since': fake.date_time_this_year().strftime('%a, %d %b %Y %H:%M:%S GMT'),
        'If-None-Match': 'W/"' + fake.sha1() + '"',
        'Sec-Ch-Ua': fake.chrome(),
        'Sec-Ch-Ua-Mobile': '?' + str(randint(0, 1)),
        'Sec-Ch-Ua-Platform': fake.random_element(elements=('Windows', 'Mac', 'Linux')),
        'Sec-Fetch-Dest': fake.random_element(elements=('document', 'image', 'script')),
        'Sec-Fetch-Mode': fake.random_element(elements=('navigate', 'no-cors', 'same-origin')),
        'Sec-Fetch-Site': fake.random_element(elements=('same-origin', 'cross-site')),
        'Sec-Fetch-User': '?' + str(randint(0, 1)),
        'Upgrade-Insecure-Requests': str(randint(0, 1)),
        'User-Agent': fake.user_agent()
    }

    return headers
# 使用代理池获取一个代理

if __name__ == '__main__':

    epoch=input("请输入访问EPOCH:")
    for i in tqdm(range(int(epoch))):
        proxy = ProxyPool.get_ip_list()
        for data in proxy:
            ip = data[0]
            headers = generate_random_headers()
            # 使用代理进行请求
            try:
                response = requests.get(target_url, proxies={'http': ip}, headers=headers)
                print('\nIP：{0}成功访问！'.format(ip))
            except requests.exceptions.RequestException as e:
                print('IP:{0}请求出错!:'.format(ip), str(e))