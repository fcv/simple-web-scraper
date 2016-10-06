import unittest
from django.test import Client
import json
from jsonpath_rw import jsonpath, parse


class HttpRequestTest(unittest.TestCase):


    def test_get(self):
        client = Client()
        response = client.get('/api/rest/v1/articles')
        self.assertEqual(response.status_code, 200)
        content = str(response.content, encoding='utf8')
        content_json = json.loads(content)

        # see more about jsonpath at http://goessner.net/articles/JsonPath/
        # and its python port at https://github.com/kennknowles/python-jsonpath-rw
        actual_ids = [match.value for match in parse('$.[*].id').find(content_json)]
        self.assertIn(1, actual_ids)
