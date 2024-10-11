import unittest
import post

class PostTest(unittest.TestCase):
    def test_get_url(self):
        post_1 = post.Post(id="1", url='https://post-1.com')

        expected = 'https://post-1.com'
        got = post_1.get_url()

        self.assertEqual(got, expected)

    def test_dict(self):
        post_1 = post.Post(id="1", url='https://post-1.com')

        expected = {
            'id': '1',
            'url': 'https://post-1.com',
            'title': None,
            'body': None,
        }
        got = post_1.dict()

        self.assertEqual(got, expected)

    def test_eq(self):
        post_1 = post.Post(id="1", url='https://post-1.com', title='post-1', body='post-1-body')
        post_2 = post.Post(id="2", url='https://post-2.com')

        self.assertFalse(post_1 == post_2)

        post_1_copy = post.Post(id="1", url='https://post-1.com', title='post-1', body='post-1-body')

        self.assertTrue(post_1 == post_1_copy)

if __name__ == '__main__':
    unittest.main()