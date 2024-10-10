import sys
import pathlib
import argparse

parser = argparse.ArgumentParser(
                    prog='BlogScraper',
                    description='Scrapes blog posts and write the results in JSON format to a file.')
parser.add_argument('--url', default='https://thejoyofcats.com')
parser.add_argument('--output-file', type=pathlib.Path, required=True)

args = parser.parse_args()

def main():
    return 0

if __name__ == '__main__':
    sys.exit(main()) 