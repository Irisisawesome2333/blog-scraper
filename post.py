class Post:
    def __init__(self, id, title, body) -> None:
        # TODO: initializes member fields for the post.
        self.id = id
        self.title = title
        self.body = body

    def dict(self) -> dict:
        """Returns a dictionary which contains attributes of the post."""
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
        }