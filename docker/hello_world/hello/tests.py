from django.test import TestCase, Client
from models import Quotes
from parse_quotes import parse_quotes
import tempfile
import os

# Create your tests here.
class TestHello(TestCase):

    @classmethod
    def setUpTestData(cls):
        q = Quotes(author="Sun Tzu", text="The best warfare strategy is to attack the enemy's plans.")
        q.save()

    def test_hello(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello World!", response.content)

    def test_quotes(self):
        client = Client()
        response = client.get('/quote/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("The best warfare strategy", response.content)

class TestParseQuotes(TestCase):

    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(delete=False)

    def tearDown(self):
        os.unlink(self.tmp.name)

    def test_parse_quotes(self):
        data = "Cookies!\tCookie Monster\n"
        self.tmp.write(data)
        self.tmp.close()
        result = list(parse_quotes(self.tmp.name))
        self.assertListEqual(result, [("Cookies!", "Cookie Monster")])

