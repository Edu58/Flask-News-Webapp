import json
import urllib.request
from .models import NewsSource, News

api_key = None
base_url = None
all_sources = None
one_source = None
search_url = None


def configure_request(app):
    global api_key, base_url, all_sources, one_source, search_url
    api_key = app.config['NEWS_APIKEY']
    base_url = app.config['NEWS_API_BASE_URL']
    all_sources = app.config['NEWS_API_ALL_SOURCES'].format(api_key)
    one_source = app.config['NEWS_API_ONE_SOURCE']
    search_url = app.config['SEARCH_NEWS_URL']


def get_all_sources():
    with urllib.request.urlopen(all_sources) as url:
        data = url.read()
        response = json.loads(data)

        sources_results = None

        if response['sources']:
            sources_results_list = response['sources']
            sources_results = process_news_sources(sources_results_list)
        else:
            return 'No results found'

    return sources_results


def process_news_sources(sources):

    modelled_data = []

    for source in sources:
        the_id = source['id']
        name = source['name']
        description = source['description']

        single_source = NewsSource(the_id, name, description)
        modelled_data.append(single_source)

    return modelled_data


def get_news(movie_id):

    one_source_url = one_source.format(movie_id, api_key)

    with urllib.request.urlopen(one_source_url) as url:
        data = url.read()
        load_json = json.loads(data)

        news_results = None

        if load_json['status'] == 'ok':
            news_list = load_json['articles']
            news_results = process_one_news(news_list)
        else:
            return 'No news found'

    return news_results


def search_keyword(keyword):

    search_base_url = search_url.format(keyword, api_key)

    with urllib.request.urlopen(search_base_url) as url:
        data = url.read()
        load_json = json.loads(data)

        search_results = None

        if load_json['status'] == 'ok':
            articles_list = load_json['articles']
            search_results = process_one_news(articles_list)
        else:
            return 'No result'

    return search_results


def process_one_news(news_list):

    modelled_news = []

    for news in news_list:
        author = news['author']
        image = news['urlToImage']
        title = news['title']
        description = news['description']
        time = news['publishedAt']
        url = news['url']

        new_news_object = News(author, image, title, description, time, url)
        modelled_news.append(new_news_object)

    return modelled_news
