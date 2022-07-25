from pprint import pprint

import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload_link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'owerwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, file_path, filename):
        href = self.upload_link(file_path=file_path).get('href', '')

        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Выполнено')


if __name__ == '__main__':

    path_to_file = ''
    token = ''

    uploader = YaUploader(token)
    uploader.upload('Файл', path_to_file)
