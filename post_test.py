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
            'date': None,
            'author': None,
            'media_urls': None,
        }
        got = post_1.dict()

        self.assertEqual(got, expected)

    def test_eq(self):
        self.assertEqual(
            post.Post(
                id="1",
                url='https://post-1.com',
                title='post-1',
                body='post-1-body',
                date='2023-12-01T09:12:24-05:00',
                author='Bob',
                media_urls=['https://test.jpg'],
            ),
            post.Post(
                id="1",
                url='https://post-1.com',
                title='post-1',
                body='post-1-body',
                date='2023-12-01T09:12:24-05:00',
                author='Bob',
                media_urls=['https://test.jpg'],
            )
        )
        self.assertNotEqual(
            post.Post(
                id="1",
                url='https://post-1.com',
                title='post-1',
                body='post-1-body',
            ),
            post.Post(
                id="2",
                url='https://post-2.com',
            )
        )

if __name__ == '__main__':
    unittest.main()