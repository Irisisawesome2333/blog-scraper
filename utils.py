import requests

RETRYABLE_STATUSES = [408, 502, 503, 504]

def get_html(url: str) -> str:
    """Returns the HTML content retrived by making an HTTP GET request to the provided URL."""
    headers = {'accept': 'text/html'}
    res = requests.get(url, headers=headers)

    # TODO: consider handling re-directions (3xx)
    if res.status_code == 200:
        return res.text

    message = "unknown error."
    if res.status_code in RETRYABLE_STATUSES:
        message = "consider retrying later."

    raise Exception("unexpected status code {status_code} received while fetching '{url}', expecting 200.\n{message}".format(
        status_code=res.status_code,
        url=url,
        message=message,
    ))
