import post
import bs4
import utils

MEDIA_TAGS = ['audio', 'embed', 'iframe', 'img', 'input', 'script', 'source', 'track', 'video']

def extract_posts(url: str) -> list[post.Post]:
    """Returns a list of post.Post containing basic information (id, url) of all posts
    found in the provided URL. Only thejoyofcats posts are supported.

    Keyword arguments:
    url -- URL to the page containing a list of available posts.
    """
    html_doc = utils.get_html(url)
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')
    posts = extracts_posts_thejoyofcats(soup)
    return posts

def scrape_posts(posts: list[post.Post]) -> None:
    """Get and scrapes the content for the given posts. Only thejoyofcats posts are supported.

    Keyword arguments:
    posts -- a list of post.Post objects each initialized with a URL value.
    """
    for post in posts:
        post_html_doc = utils.get_html(post.get_url())
        post_soup = bs4.BeautifulSoup(post_html_doc, 'html.parser')
        scrape_post_thejoyofcats(post, post_soup)

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
    date = article.find('time', {'class': 'entry-date published'})['datetime']
    author = article.find('span', {'class': 'author-name'}).get_text()

    post.set_title(title)
    post.set_body(body)
    post.set_date(date)
    post.set_author(author)
    scrape_post_media_thejoyofcats(post, soup)

def scrape_post_media_thejoyofcats(post: post.Post, soup: bs4.BeautifulSoup) -> None:
    media_urls = []
    article = soup.find(id='main').find('article')

    for tag in MEDIA_TAGS:
        for element in article.find_all(tag):
            src = element.get('src')
            if src:
                media_urls.append(src)
    
    post.set_media_urls(media_urls)
