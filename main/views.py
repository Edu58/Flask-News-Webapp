from flask import render_template, redirect, request
from . import main
from app import requests
from .search import MyForm


@main.route('/')
def index():

    all_sources = requests.get_all_sources()

    return render_template('index.html', sources=all_sources)


@main.route('/<movie_id>')
def one_source(movie_id):

    news_from_selected_choice = requests.get_news(movie_id)

    return render_template('news.html', news=news_from_selected_choice)


@main.route('/search', methods=['GET', 'POST'])
def search():
    form = MyForm()

    if request.method == "POST":
        if form.validate_on_submit():
            search_term = form.data.get('keyword')
            search_responses = requests.search_keyword(search_term)
            return render_template('search.html', form=form, response=search_responses)
        else:
            return "No results"

    return render_template('search.html', form=form)


@main.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


@main.errorhandler(500)
def not_found(e):
    return render_template('500.html'), 500
