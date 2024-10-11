import unittest
import post

class PostTest(unittest.TestCase):
    def test_get_url(self):
        new_post = post.Post("123", 'https://test.com')

        expected = 'https://test.com'
        got = new_post.get_url()

        self.assertEqual(got, expected)

if __name__ == '__main__':
    unittest.main()