class Config:
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources'
    NEWS_API_ALL_SOURCES = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    NEWS_API_ONE_SOURCE = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    SEARCH_NEWS_URL = 'https://newsapi.org/v2/everything?q={}&sortBy=popularity&apiKey={}'


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources'
    NEWS_API_ALL_SOURCES = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    NEWS_API_ONE_SOURCE = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    SEARCH_NEWS_URL = 'https://newsapi.org/v2/everything?q={}&sortBy=popularity&apiKey={}'


config_option = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'default': DevConfig
}
