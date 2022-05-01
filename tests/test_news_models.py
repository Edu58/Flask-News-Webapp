import unittest
from models import News


class TestNews(unittest.TestCase):
    def setUp(self) -> None:
        self.news = News('edwin', 'https://edwin.png', 'lunch news', 'lunch at news', '22-03-01:12:02', 'https://edwin.media.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.news, News))


if __name__ == '__main__':
    unittest.main()
