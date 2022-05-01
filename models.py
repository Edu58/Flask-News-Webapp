class NewsSource:

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


class News:

    def __init__(self, image, description, time, url):
        self.image = image
        self.description = description
        self.time = time
        self.url = url
