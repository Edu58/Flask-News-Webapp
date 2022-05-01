import json
import urllib.request
from .models import NewsSource, News

api_key = None
base_url = None
all_sources = None


def configure_request(app):
    global api_key, base_url, all_sources
    api_key = app.config['NEWS_APIKEY']
    base_url = app.config['NEWS_API_BASE_URL']
    all_sources = app.config['NEWS_API_ALL_SOURCES'].format(api_key)


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
