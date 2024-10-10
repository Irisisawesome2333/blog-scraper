import sys
import pathlib
import argparse
import scrape
import json
import requests
import bs4

parser = argparse.ArgumentParser(
                    prog='BlogScraper',
                    description='Scrapes blog posts and write the results in JSON format to a file.')
parser.add_argument('--url', default='https://thejoyofcats.com')
parser.add_argument('--output-file', type=pathlib.Path, required=True)

args = parser.parse_args()

def get_html(url:str) -> str:
    """Makes an HTTP GET request to the provided URL to request HTML content."""
    headers = {'accept': 'text/html'}
    res = requests.get(url, headers=headers)

    # TODO: consider handling re-directions (3xx)
    if res.status_code != 200:
        raise Exception("unexpected status code {res.status_code} received while fetching '{url}', expecting 200.")
    return res.text

def main():
    html_doc = get_html(args.url)
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')
    posts = scrape.extract_posts_thejoyofcats(soup)
    data = [post.dict() for post in posts]

    with open(args.output_file, 'w') as f:
        json.dump(data, f)

    return 0

if __name__ == '__main__':
    sys.exit(main()) 