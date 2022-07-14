from time import sleep

from pyuseragents import random as random_useragent
from requests import Session
from random import choice

delay = 5
print("Софт от лучшего канала - https://t.me/cryptoblinchik")
print("Почты должны быть в виде: email или email:password")
file = input("Введите названия файла с почтами (файл должен находиться в папке с файлом скрипта): ")
use_proxy = input('Use Proxies? (y/N): ').lower()
if use_proxy == 'y':
    delay = 0
    proxy_type = str(input('Enter proxy type (http; https; socks4; socks5): '))
    proxy_folder = str(input('Drag and drop file with proxies (ip:port): '))
    proxies = []
    with open(proxy_folder, 'r') as file_2:
        for row in file_2:
            proxies.append(row.strip())
with open(file) as f:
    for i in f.readlines():
        email = i.split(":")[0]
        session = Session()
        session.headers.update({'user-agent': random_useragent(),
                                'accept': 'application/json, text/javascript, */*; q=0.01',
                                'accept-language': 'ru,en;q=0.9',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'origin': 'https://trade.polynomial.fi',
                                'referer': 'https://trade.polynomial.fi/'
                                })
        if use_proxy == 'y':
            proxy = choice(proxies)
            session.proxies.update({'http': f'{proxy_type}://{proxy}', 'https': f'{proxy_type}://{proxy}'})
        r = session.post("https://webflow.com/api/v1/form/62ac1f5760c936dfdeabd4b9",
                         data={'name': 'Email Form',
                               'source': 'https://trade.polynomial.fi/#Waitlist',
                               'test': 'false',
                               'fields[Email]': email,
                               'dolphin': 'false'})
        sleep(delay)
        if r.ok:
            print(email, "on the waitlist")
        else:
            print(email, "error")
