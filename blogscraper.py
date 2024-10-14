import sys
import pathlib
import argparse
import scrape
import json
from post import Post

parser = argparse.ArgumentParser(
                    prog='BlogScraper',
                    description='Scrapes blog posts from and write the results in JSON format to a file.')
parser.add_argument('--url', default='https://thejoyofcats.com', help='The URL of the blog page to scrape. Only thejoyofcats blog pages are supported.')
parser.add_argument('--output-file', type=pathlib.Path, required=True, help='The output file to write the scraped data to, in JSON format.')

args = parser.parse_args()

def dump_posts(posts: list[Post], output_file: pathlib.Path) -> None:
    """Writes posts data to the given output file in JSON format."""
    data = [post.dict() for post in posts]
    with open(output_file, 'w') as f:
        json.dump(data, f)

def main():
    posts = scrape.extract_posts(args.url)
    scrape.scrape_posts(posts)
    dump_posts(posts, args.output_file)

    return 0

if __name__ == '__main__':
    sys.exit(main()) 