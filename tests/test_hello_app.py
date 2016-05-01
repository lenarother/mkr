from selenium import webdriver
from unittest import TestCase, main


class HelloWorldAppTests(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_body(self):
        self.driver.get("http://127.0.0.1:8000")
        self.assertTrue('Hello World!' in self.driver.page_source)

    def test_quote(self):
        self.driver.get("http://127.0.0.1:8000/quote")
        self.assertTrue('Sun Tzu' in self.driver.page_source)

if __name__ == "__main__":
    main()