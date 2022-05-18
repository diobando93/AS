from http.client import PROCESSING
import unittest
import requests


class FlaskTest(unittest.TestCase):

    def test_search_provider_by_id(self):
        API_URL = "http://127.0.0.1:3000"
        PROVIDER_URL = "{}/provider?provider=21".format(API_URL)
        r = requests.get(PROVIDER_URL)
        self.assertEqual(r.status_code, 200)

    def test_search_provider_by_ip(self):
        API_URL = "http://127.0.0.1:3000"
        PROVIDER_URL = "{}/provider?provider=1.2.3.4".format(API_URL)
        r = requests.get(PROVIDER_URL)
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
