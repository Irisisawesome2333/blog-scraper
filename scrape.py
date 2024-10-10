import post
import bs4

def extract_posts(soup: bs4.BeautifulSoup) -> list[post.Post]:
    """Returns a list of post.Post objects extracted from the provided BeautifulSoup
        instance representing an HTML document.

    Keyword arguments:
    html_doc -- the HTML content of https://thejoyofcats.com
    """
    # TODO: extract posts from provide html
    return [post.Post()]