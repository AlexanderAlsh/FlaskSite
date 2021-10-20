import unittest
import requests


class ApiTest(unittest.TestCase):
    URL_API = 'http://127.0.0.1:5000'
    URL_GET_ALL = '{}/show_data_all'.format(URL_API)
    URL_ADD_NEW = '{}/create_data'.format(URL_API)
    URL_GET_ONE = '{}/show_data_by_id'.format(URL_API)
    URL_UPDATE = '{}/update_data'.format(URL_API)
    URL_DELETE = '{}/delete_data'.format(URL_API)

    def test_1_get_all(self):
        r = requests.get(ApiTest.URL_GET_ALL)
        self.assertEqual(r.status_code, 200)


    def test_2_add_new_word(self):
        obj_add = {'word': 'Hola', 'translate': 'Привки'}
        r = requests.post(ApiTest.URL_ADD_NEW, data=obj_add)
        self.assertEqual(r.status_code, 200)

    def test_3_get_one_word(self):
        obj_get_one = {'data_id': '2'}
        r = requests.post(ApiTest.URL_GET_ONE, data=obj_get_one)
        self.assertEqual(r.status_code, 200)


    def test_4_update(self):
        obj_update = {'word1': 'Hola', 'word2': 'Чан'}
        r = requests.post(ApiTest.URL_UPDATE, data=obj_update)
        self.assertEqual(r.status_code, 200)

    def test_5_delete(self):
        obj_delete = {'word1': 'Hola'}
        r = requests.post(ApiTest.URL_DELETE, data=obj_delete)
        self.assertEqual(r.status_code, 200)