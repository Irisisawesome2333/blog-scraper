class Post:
    # TODO: add docstring description for the class
    def __init__(self,
                id: str = None,
                url: str = None,
                title: str = None,
                body: str = None,
    ) -> None:
        self.id = id
        self.url = url
        self.title = title
        self.body = body

    def __eq__(self, other: object) -> bool:
        return self.id == other.id and \
            self.url == other.url and \
            self.title == other.title and \
            self.body == other.body

    def dict(self) -> dict:
        """Returns a dictionary which contains attributes of the post."""
        return {
            'id': self.id,
            'url': self.url,
            'title': self.title,
            'body': self.body,
        }

    def get_url(self) -> str:
        return self.url

    def set_title(self, title: str):
        self.title = title

    def set_body(self, body: str):
        self.body = body