import unittest
import scrape
import post
from bs4 import BeautifulSoup

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
''')
        expected = [post.Post(id='1', url='https://post-1'), post.Post(id='2', url='https://post-2')]
        got = scrape.extracts_posts_thejoyofcats(soup)

        self.assertListEqual(got, expected)

if __name__ == '__main__':
    unittest.main()