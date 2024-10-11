import unittest
import utils
import requests_mock

TEST_URL = 'http://test.com'

class UtilsTest(unittest.TestCase):
    def test_get_html_returns_text(self):
        with requests_mock.Mocker() as m:
            m.get(TEST_URL, text='data')

            expected = 'data'
            got = utils.get_html(TEST_URL)
            self.assertEqual(got, expected)

    def test_get_html_errors(self):
        with requests_mock.Mocker() as m:
            m.get(TEST_URL, status_code=404)

            with self.assertRaises(Exception):
                utils.get_html(TEST_URL)

    def test_get_html_retryable_errors(self):
        with requests_mock.Mocker() as m:
            m.get(TEST_URL, status_code=502)

            with self.assertRaisesRegex(Exception, 'retrying later'):
                utils.get_html(TEST_URL)

if __name__ == '__main__':
    unittest.main()