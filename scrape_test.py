import unittest
import scrape
import post
from bs4 import BeautifulSoup
from unittest.mock import patch

class PostTest(unittest.TestCase):
    def test_extracts_posts_thejoyofcats(self):
        soup = BeautifulSoup('''
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
                ''', 'html.parser')
        expected = [post.Post(id='1', url='https://post-1'), post.Post(id='2', url='https://post-2')]
        got = scrape.extracts_posts_thejoyofcats(soup)

        self.assertListEqual(got, expected)

    def test_scrape_post_thejoyofcats(self):
        soup = BeautifulSoup('''
                <!DOCTYPE html>
                <html>
                <body>
                <main id='main'>
                    <article id="post-1">
                        <header>
                            <h1>post-1 title</h1>
                        </header>
                        <div class='entry-content'>post-1 body</div>
                        <time class='entry-date published' datetime='2024-10-11'>2024-10-11</time>
                        <span class='author-name'>author name</span>
                    </article>
                </main>
                </body>
                </html>
                ''', 'html.parser')
        post_1 = post.Post(id='1', url='https://post-1')

        scrape.scrape_post_thejoyofcats(post_1, soup)

        expected_post = post.Post(id='1', url='https://post-1', title='post-1 title', body='post-1 body', date='2024-10-11', author='author name', media_urls=[])
        self.assertEqual(post_1, expected_post)

    @patch('utils.get_html')
    def test_extract_posts(self, get_html_mock):
        posts = [post.Post(id='1', url='https://post-1'), post.Post(id='2', url='https://post-2')]
        get_html_mock.return_value = '''
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
        
        got =scrape.extract_posts(posts)
        expected = [post.Post(id='1', url='https://post-1'),
                         post.Post(id='2', url='https://post-2')]
        
        self.assertListEqual(got, expected)

    @patch('utils.get_html')
    def test_scrape_posts(self, get_html_mock):
        posts = [post.Post(id='1', url='https://post-1'), post.Post(id='2', url='https://post-2')]
        get_html_mock.side_effect = ['''
               <!DOCTYPE html>
                <html>
                <body>
                <main id='main'>
                    <article id="post-1">
                        <header>
                            <h1>post-1 title</h1>
                        </header>
                        <div class='entry-content'>post-1 body</div>
                        <time class='entry-date published' datetime='2024-10-11'>2024-10-11</time>
                        <span class='author-name'>author name</span>
                    </article>
                </main>
                </body>
                </html>
                ''', '''
                <!DOCTYPE html>
                <html>
                <body>
                <main id='main'>
                    <article id="post-2">
                        <header>
                            <h1>post-2 title</h1>
                        </header>
                        <div class='entry-content'>post-2 body</div>
                        <time class='entry-date published' datetime='2024-10-11'>2024-10-11</time>
                        <span class='author-name'>author name</span>
                    </article>
                </main>
                </body>
                </html>
                ''']
        
        scrape.scrape_posts(posts)
        expected_posts = [post.Post(id='1', url='https://post-1', title='post-1 title', body='post-1 body', date='2024-10-11', author='author name', media_urls=[]),
                         post.Post(id='2', url='https://post-2', title='post-2 title', body='post-2 body', date='2024-10-11', author='author name', media_urls=[])]
        
        self.assertListEqual(posts, expected_posts)  

if __name__ == '__main__':
    unittest.main()