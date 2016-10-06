import unittest
from django.test import Client


class HttpRequestTest(unittest.TestCase):


    def test_get(self):
        client = Client()
        response = client.get('/api/rest/v1/articles')
        self.assertEqual(response.status_code, 200)
