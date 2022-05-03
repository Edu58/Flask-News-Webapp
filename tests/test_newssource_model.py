import unittest
from app.models import NewsSource


class TestNewsSource(unittest.TestCase):
    def setUp(self) -> None:
        self.news = NewsSource('kbc', 'kenya broadcasting corporation', 'a government owned media house')

    def test_instance(self):
        self.assertTrue(isinstance(self.news, NewsSource))


if __name__ == '__main__':
    unittest.main()
