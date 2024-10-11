class Post:
    """
    A class representing a post on a blog webpage.

    Attributes:
        id : str, default None
            A unique identifier for the post.
        url : str, default None
            The URL of the blog post.
        title : str, default None
            The title of the blog post.
        body : str, default None
            The main content/body of the blog post.
        date : str, default None
            The publication date of the blog post.
        author : str, default None
            The author of the blog post.
        media_urls : list[str], default None
            A list of media URLs (e.g., images, videos) associated with the post body.
    """

    def __init__(self,
                id: str = None,
                url: str = None,
                title: str = None,
                body: str = None,
                date: str = None,
                author: str = None,
                media_urls: list[str]= None,
    ) -> None:
        self.id = id
        self.url = url
        self.title = title
        self.body = body
        self.date = date
        self.author = author
        self.media_urls = media_urls

    def __eq__(self, other: object) -> bool:
        return self.id == other.id and \
            self.url == other.url and \
            self.title == other.title and \
            self.body == other.body and \
            self.date == other.date and \
            self.author == other.author and \
            self.media_urls == other.media_urls

    def dict(self) -> dict:
        """Returns a dictionary which contains attributes of the post."""
        return {
            'id': self.id,
            'url': self.url,
            'title': self.title,
            'body': self.body,
            'date': self.date,
            'author': self.author,
            'media_urls': self.media_urls
        }

    def get_url(self) -> str:
        return self.url

    def set_title(self, title: str):
        self.title = title

    def set_body(self, body: str):
        self.body = body

    def set_date(self, date: str):
        self.date = date

    def set_author(self, author: str):
        self.author = author
    
    def set_media_urls(self, media_urls: list[str]):
        self.media_urls = media_urls