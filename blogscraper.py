import sys
import pathlib
import argparse
import scrape
import json
import bs4
import utils
import post

parser = argparse.ArgumentParser(
                    prog='BlogScraper',
                    description='Scrapes blog posts and write the results in JSON format to a file.')
parser.add_argument('--url', default='https://thejoyofcats.com')
parser.add_argument('--output-file', type=pathlib.Path, required=True)

args = parser.parse_args()

def extract_posts(url: str) -> list[post.Post]:
    """Returns a list of post.Post containing basic information (id, url) of all posts
        found in the provided URL. Only thejoyofcats posts are supported.

    Keyword arguments:
        url -- URL to the page containing a list of available posts.
    """
    html_doc = utils.get_html(url)
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')
    posts = scrape.extracts_posts_thejoyofcats(soup)
    return posts

def scrape_posts(posts: list[post.Post]) -> None:
    """Get and scrapes the content for the given posts. Only thejoyofcats posts are supported.

    Keyword arguments:
        posts -- a list of post.Post objects each initialized with a URL value.
    """
    for post in posts:
        post_html_doc = utils.get_html(post.get_url())
        post_soup = bs4.BeautifulSoup(post_html_doc, 'html.parser')
        scrape.scrape_post_thejoyofcats(post, post_soup)

def dump_posts(posts: list[post.Post], output_file: pathlib.Path) -> None:
    """Writes posts data to the given output file in JSON format."""
    data = [post.dict() for post in posts]
    with open(output_file, 'w') as f:
        json.dump(data, f)

def main():
    posts = extract_posts(args.url)
    scrape_posts(posts)
    dump_posts(posts, args.output_file)

    return 0

if __name__ == '__main__':
    sys.exit(main()) 