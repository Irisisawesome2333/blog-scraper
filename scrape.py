import post
import bs4

def extract_posts_thejoyofcats(soup: bs4.BeautifulSoup) -> list[post.Post]:
    """Returns a list of post.Post objects extracted from the provided BeautifulSoup
        instance representing a thejoyofcats HTML document.

    Keyword arguments:
    soup -- a BeautifulSoup instance representing the HTML content of https://thejoyofcats.com.
    """
    posts = []
    articles = soup.find(id='main').find_all('article')

    for article in articles:
        title_a = article.find('header').find('a')
        summary_p = article.find('div', {'class': 'entry-summary'}).find('p')

        # TODO: extract number from id string
        id = article.attrs['id']
        title = title_a.get_text()
        body = summary_p.get_text()

        posts.append(post.Post(id=id, title=title, body=body))

    return posts