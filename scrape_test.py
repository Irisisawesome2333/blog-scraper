import unittest
import scrape
from post import Post
from bs4 import BeautifulSoup
from unittest.mock import patch

class PostTest(unittest.TestCase):
    @patch('utils.get_html')
    def test_extract_posts_thejoyofcats(self, get_html_mock):
        mocked_html = {
            'https://thejoyofcats': '''
<!DOCTYPE html>
<html>
<body>
<main id='main'>
    <article id="post-1">
        <header>
            <a href="https://post-1"></a>
        </header>
    </article>
    <article id="post-2">
        <header>
            <a href="https://post-2"></a>
        </header>
    </article>
</main>
</body>
</html>
'''
        }
        get_html_mock.side_effect = lambda url: mocked_html[url]

        got = scrape.extract_posts('https://thejoyofcats')
        expected = [Post(id='1', url='https://post-1'), Post(id='2', url='https://post-2')]
        # Sort the posts by id to ensure the order is consistent.
        expected.sort(key=lambda p: p.id)
        got.sort(key=lambda p: p.id)
        self.assertListEqual(got, expected)

    @patch('utils.get_html')
    def test_scrape_posts_thejoyofcats(self, get_html_mock):
        mocked_html = {
            'https://post-1': '''
<!DOCTYPE html>
<html>
<body>
<main id='main'>
    <article id="post-1">
        <header>
            <h1>post-1 title</h1>
        </header>
        <div class='entry-content'>post-1 body</div>
        <time class='entry-date published' datetime='2023-12-01T09:12:24-05:00'>Dec 2023</time>
        <span class='author-name'>author name</span>
    </article>
</main>
</body>
</html>
''',
            'https://post-2': '''
<!DOCTYPE html>
<html>
<body>
<main id='main'>
    <article id="post-2">
        <header>
            <h1>post-2 title</h1>
        </header>
        <div class='entry-content'>post-2 body</div>
        <time class='entry-date published' datetime='2023-12-01T09:12:24-05:00'>Dec 2023</time>
        <span class='author-name'>author name</span>
        <img src="https://test.jpg"></img>
        <video src="https://test.mp4"></video> 
    </article>
</main>
</body>
</html>
'''
        }
        get_html_mock.side_effect = lambda url: mocked_html[url]

        expected = [
            Post(id='1', url='https://post-1', title='post-1 title', body='post-1 body', 
                date='2023-12-01T09:12:24-05:00', author='author name', media_urls=[]),
            Post(id='2', url='https://post-2', title='post-2 title', body='post-2 body', 
                date='2023-12-01T09:12:24-05:00', author='author name', media_urls=["https://test.jpg", "https://test.mp4"])
        ]
        posts = [Post(id='1', url='https://post-1'), Post(id='2', url='https://post-2')]
        scrape.scrape_posts(posts)
        got = posts
        # Sort the posts by id to ensure the order is consistent.
        expected.sort(key=lambda p: p.id)
        got.sort(key=lambda p: p.id)
        self.assertListEqual(got, expected)

if __name__ == '__main__':
    unittest.main()