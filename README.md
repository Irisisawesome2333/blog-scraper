# BlogScraper

Blogscraper is a program for scraping blog posts from [http://thejoyofcats.com](http://thejoyofcats.com). By default, the program scrapes the first page of the site, but it can also be customized to scrape other pages by passing different `--url` parameters. See below for examples.

The output of the program contains the following attributes for each post it scrapes, in JSON format:

- `id`: Unique post identifier
- `url`: Post URL
- `title`: Post title
- `body`: Post body
- `date`: Post date
- `author`: Post author
- `media_urls`: A list of media URLs for any media in the post body

## Requirements

To run this program, the following software packages are required:
- Python 3.9+
- pip

## Run program

Before running the program, ensure the current working directory is the project root directory.

```bash
cd <project_directory>
```

### Set up virtual environment (optional but recommended)

It is recommanded to use an [virtual environment](https://python.land/virtual-environments/virtualenv) to isolate packages from the global environment.

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install packages
```bash
pip install -r requirements.txt
```

### Scrape thejoyofcats's first page

Run the following commands to scrape the first page of http://thejoyofcats.com and save the output to `/tmp/out.json`.

```bash
OUTPUT_FILE=/tmp/out.json
python blogscraper.py --output-file=${OUTPUT_FILE?}
```

### Scrape other pages

Provide a `--url` flag to scrape a different page. For example, to scrape the second page of the site:

```bash
OUTPUT_FILE=/tmp/out.json
python blogscraper.py --output-file=${OUTPUT_FILE?} --url=https://thejoyofcats.com/page/2
```

### Help

To print a help message, run:

```bash
python blogscraper.py --help
```

## Development

### Run unit tests
To run all unit test files for this project, use the following command:

```bash
python -m unittest discover -p "*_test.py"
```

## Support other websites

At this time, the program only support scraping blog posts from thejoyofcats. There is no plan on supporting other blog platforms. That being said, transforming the program to support a different website should be easy and involves roughly the following steps:

1. Implement `extracts_posts_<website>` and `scrape_post_.*<website>` functions in `scrape.py`.
1. Call the implemented functions from the program's entry `blogscraper.py`.


## Tradeoffs

The following tradeoffs were made while desiging this program.

### HTTP error handling

It is possible for the program to see transient HTTP errors while making frequent requests to a Website. In some cases, these errors are retryable. This means even though one request failed, but a subsequent one made at a later time may succeed.

|| Simple handling (adpoted)    | Automatic retry |
|---| -------- | ------- |
| Description | Exits when unexpected HTTP status code is received. If an error is potentially retriable, print a message to tell the user to retry. |  The program automatically retry an HTTP request on potential retryable errors with exponetial backoff.   |
| Pros | Easy to implement; Behaviour is predictable. |  More robust; User-friendly.    |
| Cons | Kiiling the program only takes one error.   |  Higher complexity. Potential unnecessary delay with exponential backoff. |

The simple error handling design is adoped since the implementation is much easier. http://thejoyofcats.com is a fairly stable website. The additional benefits of a more complex implementation is likely insignificant.

### Throttling

To be responsible and not abuse the website being scraped, the frequency of the requests sent by scraper should be in a acceptable range. In some cases, the scraper may get throttled (or banned) by a Web server if large volume of requests were made within a short period of time. This can be avoided by implementing a throttling mechanism to limit the request frequency.

Given that each thejoyofcats page contains ~10 blog posts, a throttling mechenism maybe an overkill. However, it is something to consider when the program is expected to scrape more posts.
