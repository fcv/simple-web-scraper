from django.test import Client, TransactionTestCase
import json
from jsonpath_rw import jsonpath, parse


class ArticleEndpointTest(TransactionTestCase):

    fixtures = ['articles_and_authors.json']
    endpoint = '/api/rest/v1/articles'

    def test_list(self):
        client = Client()
        response = client.get(ArticleEndpointTest.endpoint)
        self.assertEqual(response.status_code, 200)
        content = str(response.content, encoding='utf8')
        content_json = json.loads(content)

        # see more about jsonpath at http://goessner.net/articles/JsonPath/
        # and its python port at https://github.com/kennknowles/python-jsonpath-rw
        actual_ids = [match.value for match in parse('$.[*].id').find(content_json)]
        self.assertEquals([1], actual_ids)

    def test_404_when_id_doesnt_exist(self):
        client = Client()
        response = client.get(ArticleEndpointTest.endpoint + '/123')
        self.assertEqual(response.status_code, 404)

    def test_post(self):
        client = Client()
        json_str = json.dumps({
            "title": "a nice title",
            "url": "http://johndoo.org",
            "content": "dummy content",
        })
        response = client.post(ArticleEndpointTest.endpoint, data=json_str, content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_delete(self):
        client = Client()
        response = client.delete(ArticleEndpointTest.endpoint + '/1')
        self.assertEqual(response.status_code, 204)

    def test_delete_not_found(self):
        client = Client()
        response = client.delete(ArticleEndpointTest.endpoint + '/123')
        self.assertEqual(response.status_code, 404)