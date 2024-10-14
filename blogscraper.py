import sys
import pathlib
import argparse
import scrape
import utils

parser = argparse.ArgumentParser(
                    prog='BlogScraper',
                    description='Scrapes blog posts from thejoyofcats and write the results in JSON format to a file.')
parser.add_argument('--url', default='https://thejoyofcats.com', help='The URL of the blog page to scrape. Only thejoyofcats blog pages are supported.')
parser.add_argument('--output-file', type=pathlib.Path, required=True, help='The output file to write the scraped data to, in JSON format.')

def main():
    args = parser.parse_args()
    posts = scrape.extract_posts(args.url)
    scrape.scrape_posts(posts)
    utils.dump_posts(posts, args.output_file)
    return 0

if __name__ == '__main__':
    sys.exit(main()) 