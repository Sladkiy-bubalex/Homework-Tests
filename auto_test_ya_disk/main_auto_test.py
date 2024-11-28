import requests
import pytest
import os
import dotenv


class TestYD:
    dotenv.load_dotenv()
    def setup_method(self):
        self.headers = {
            'Authorization': os.getenv('TOKEN_YA_DISK')
        }
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
    
    def test_status_code_200(self):
        response = requests.get('https://cloud-api.yandex.net/v1/disk', headers=self.headers)
        assert response.status_code == 200

    @pytest.mark.parametrize(
        'param, folder_name, status_code',
        [('path', 'test', 201),
         ('fields', 'test_2', 400),
         ('path', 'test', 409)
         ]
    )
    def test_create_folder(self, param, folder_name, status_code):
        params = {
            param: folder_name
        }
        response = requests.put(self.url, params=params, headers=self.headers)
        assert response.status_code == status_code