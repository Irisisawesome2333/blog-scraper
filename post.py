class Post:
    # TODO: add docstring description for the class
    id = None
    url = None
    title = None
    body = None

    def __init__(self, id: str, url: str) -> None:
        self.id = id
        self.url = url

    def dict(self) -> dict:
        """Returns a dictionary which contains attributes of the post."""
        return {
            'id': self.id,
            'title': self.title,
            'url': self.url,
            'body': self.body,
        }

    def get_url(self) -> str:
        return self.url

    def set_title(self, title: str):
        self.title = title

    def set_body(self, body: str):
        self.body = body