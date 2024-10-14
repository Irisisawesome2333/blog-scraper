# BlogScraper

Blogscraper is a program for scraping blog posts from [http://thejoyofcats.com](http://thejoyofcats.com). By default, the program scrapes the first page of the site, but it can also be customized to scrape other pages by passing different `--url` parameters. See below for examples.

The output of the program contains the following attributes for each post it scrapes, in JSON format:

- `id`: Unique post identifier
- `url`: Post URL
- `title`: Post title
- `body`: Post body
- `date`: Post date
- `author`: Post author
- `media_urls`: A list of media URLs for any image in the post body

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

It is recommended to use a [virtual environment](https://python.land/virtual-environments/virtualenv) to isolate packages from the global environment.

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install packages
```bash
pip install -r requirements.txt
```

### Scrape the first page of thejoyofcats

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

At this time, the program only supports scraping blog posts from thejoyofcats. There is no plan to support other blog platforms. That being said, transforming the program to support a different website should be easy and involves roughly the following steps:

1. Implement `extracts_posts_<website>` and `scrape_post_<website>` functions in `scrape.py`.
1. Call the newly implemented functions in the `extract_posts` and `scrape_posts` functions.
1. (Optional) use command line arguments to decide which website to scrape.


## Tradeoffs

The following tradeoffs were made while desiging this program.

### HTTP error handling

It is possible for the program to encounter transient HTTP errors while making frequent requests to a Website. In some cases, these errors are retryable, meaning that even though one request fails, a subsequent one made at a later time may succeed.

|| Simple handling (adpoted)    | Automatic retry |
|---| -------- | ------- |
| Description | Exits when an unexpected HTTP status code is received. If an error is potentially retriable, a message is printed to inform the user to retry. |  The program automatically retries an HTTP request on potential retriable errors with exponential backoff.   |
| Pros | Easy to implement; behaviour is predictable. |  More robust; User-friendly.    |
| Cons | One error can terminate the program.   |  Higher complexity. Potential unnecessary delay with exponential backoff. |

The simple error-handling design is adoped since the implementation is much easier. http://thejoyofcats.com is a fairly stable website, and the additional benefits of a more complex implementation are likely insignificant.

### Throttling

To avoid abusing the website being scraped, the frequency of the requests sent by the scraper should be within an acceptable range. In some cases, the scraper may get throttled (or banned) by a Web server if a large volume of requests is made in a short period of time. This can be mitigated by implementing a throttling mechanism to limit request frequency.

Given that each blog page of thejoyofcats contains around 10 blog posts, a throttling mechanism may be overkill. However, it is something to consider if the program is expected to scrape more posts in the future.
