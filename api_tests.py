import os

import sys

sys.path.insert(0, 'api')

# from api import app

import unittest

import tempfile


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        api.app.testing = True
        self.app = api.app.test_client()

    # def test_home_page(self):
    #     rv = self.api.get('/')
    #     assert b'No entries here so far' in rv.data


if __name__ == '__main__':
    unittest.main()
