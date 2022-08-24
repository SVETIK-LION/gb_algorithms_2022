"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""


import hashlib
from uuid import uuid4


cache_url = {}
salt = uuid4().hex


def check_cache(url):
    if cache_url.get(url):
        print(f'Адрес {url} уже записан в кэш с хэшем: {cache_url[url]}')
    else:
        hash_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_url[url] = hash_url
        print(cache_url)


check_cache('https://fallout.fandom.com/wiki/Fallout_Wiki')
check_cache('https://fallout.fandom.com/wiki/Fallout_Wiki')
check_cache('https://ru.wikipedia.org/wiki/%D0%98%D0%BD%D1%8C_%D0%B8_%D1%8F%D0%BD')
