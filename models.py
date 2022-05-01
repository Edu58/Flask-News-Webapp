class NewsSource:

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


class News:

    def __init__(self, author, image, title, description, time, url):
        self.author = author
        self.image = image
        self.title = title
        self.description = description
        self.time = time
        self.url = url
