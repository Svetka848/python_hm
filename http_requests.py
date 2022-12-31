#!/usr/bin/python
#  -*- coding: utf-8 -*-

import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str, href: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        with open(file_path, "rb") as file:
            response = requests.put(href, data=file)
            if response.status_code == 201:
                print("Файл загружен")
                return True
            print("Файл не загружен, потому что", response.status_code)
            return False


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    href = 'https://uploader20o.disk.yandex.net:443/upload-target/20221231T205753.152.utd.b5wrkdui45rflo4iq5l5m2kgd-k20o.3911770'
    path_to_file = r"C:\Users\svetl\photo1670677333.jpeg"
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, href)