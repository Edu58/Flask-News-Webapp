from flask import render_template, url_for
from . import main
from app import requests


@main.route('/')
def index():

    all_sources = requests.get_all_sources()

    return render_template('index.html', sources=all_sources)


@main.route('/<str:id>')
def one_source(id):

    news_from_selected_choice = requests.get_news(id)

    return render_template('news.html', news=news_from_selected_choice)
