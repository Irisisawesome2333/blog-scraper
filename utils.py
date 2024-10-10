import requests

def get_html(url: str) -> str:
    """Returns the HTML content retrived by making an HTTP GET request to the provided URL."""
    headers = {'accept': 'text/html'}
    res = requests.get(url, headers=headers)

    # TODO: consider handling re-directions (3xx)
    # TODO: consider handling retryable errors
    if res.status_code != 200:
        raise Exception("unexpected status code {res.status_code} received while fetching '{url}', expecting 200.")
    return res.text