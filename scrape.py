import post
import bs4

def extracts_posts_thejoyofcats(soup: bs4.BeautifulSoup) -> list[post.Post]:
    """Returns a list of post.Post objects extracted from the provided BeautifulSoup
        instance representing a thejoyofcats HTML document.

    Keyword arguments:
        soup -- a BeautifulSoup instance representing the HTML content of https://thejoyofcats.com.
    """
    posts = []
    articles = soup.find(id='main').find_all('article')

    for article in articles:
        title_a = article.find('header').find('a')
        id = article.attrs['id'].replace('post-', '')
        url = title_a.attrs['href']

        posts.append(post.Post(id=id, url=url))

    return posts

def scrape_post_thejoyofcats(post: post.Post, soup: bs4.BeautifulSoup) -> None:
    """Scrapes post information from the provided HTML content and sets the information
        for the provided post object.

    Keyword arguments:
        post -- a post.Post instance initialized with a post URL.
        soup -- a BeautifulSoup instance containing the HTML content of a https://thejoyofcats.com post.
    """
    article = soup.find(id='main').find('article')
    title = article.find('header').find('h1').get_text()
    body = article.find('div', {'class': 'entry-content'}).get_text()

    post.set_title(title)
    post.set_body(body)