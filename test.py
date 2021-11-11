from unittest import TestCase
from app import app
from flask import jsonify
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
class FlaskTests(TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_show_homepage(self):
        """test initial page"""
        with self.client as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)

    def test_convert_currency(self):
        """
        test currency convert functions
        test result number and code
        """
        with self.client as client:
            res = client.post('/result', 
                 data={'currency': 'USD',
                 'newCurrency': 'CNY',
                 'amount': '100'})
            # log = logging.getLogger('test')
            # log.debug(res.data)
            self.assertIn(b'639.09', res.data)
            # self.assertIn(b'¥', res.data)
            # self.assertEqual(b'res.data.code', ¥)

    def test_not_a_currency(self):
        """
        test currency convert functions
        test result number and code
        """
        with self.client as client:
            res = client.post('/result', 
                 data={'currency': 'EBC',
                 'newCurrency': 'CNY',
                 'amount': '100'})
            self.assertIn(b'EBC is not a valid currency', res.data)

    def test_not_a_currency2(self):
        """
        test currency convert functions
        test alert msg
        """
        with self.client as client:
            res = client.post('/result', 
                 data={'currency': 'USD',
                 'newCurrency': 'UEC',
                 'amount': '100'})
            self.assertIn(b'UEC is not a valid currency', res.data)

    def test_not_valid_number(self):
        """
        test currency convert functions
        test result number and code
        """
        with self.client as client:
            res = client.post('/result', 
                 data={'currency': 'USD',
                 'newCurrency': 'CNY',
                 'amount': 'AA'})
            self.assertIn(b'AA is not a valid number', res.data)

    def test_not_valid(self):
        """
        test currency convert functions
        test result number and code
        """
        with self.client as client:
            res = client.post('/result', 
                 data={'currency': 'EBC',
                 'newCurrency': 'USC',
                 'amount': 'AA'})
            self.assertIn(b'EBC is not a valid currency', res.data)
            self.assertIn(b'USC is not a valid currency', res.data)
            self.assertIn(b'AA is not a valid number', res.data)


 

