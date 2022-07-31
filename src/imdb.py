import requests as r
from typing import List


class Imdb:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = 'https://imdb-api.com/en/API'

    def search_movies(self, name: str) -> List['Movie']:
        movies = []
        url = '{0}/SearchMovie/{1}/{2}'.format(
            self.base_url, self.api_key, name)

        response = r.get(url)

        if (response.status_code == 200):
            response_obj = response.json()

            for movie in response_obj:
                movies.append(Movie(
                    movie['id'],
                    movie['title'],
                    movie['description'],
                    movie['image']
                ))

        return movies

    def search_title(self, title_id: str) -> 'Title':
        url = '{0}/Title/{1}/{2}'.format(
            self.base_url, self.api_key, title_id)

        response = r.get(url)

        if (response.status_code == 200):
            response_obj = response.json()
            return Title(
                response_obj['fullTitle'],
                response_obj['genres'],
                response_obj['languages'],
                response_obj['type'],
                response_obj['year'],
                response_obj['image'],
                response_obj['runtimeStr'],
                response_obj['plot'],
                response_obj['directors'],
                response_obj['stars'],
                response_obj['contentRating'],
                response_obj['imDbRating'],
                response_obj['imDbRatingVotes'],
                response_obj['metacriticRating']
            )


class Movie:
    def __init__(self, id, title, description, image_url) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.image_url = image_url


class Title:
    def __init__(self, full_title, genre, language, type, year, image_url, runtime, plot, directors, stars, content_rating, imdb_rating, imdb_votes, metacritic_rating) -> None:
        self.full_title = full_title
        self.genre = genre
        self.language = language
        self.type = type
        self.year = year
        self.image_url = image_url
        self.runtime = runtime
        self.plot = plot
        self.directors = directors
        self.stars = stars
        self.content_rating = content_rating
        self.imdb_rating = imdb_rating
        self.imdb_votes = imdb_votes
        self.metacritic_rating = metacritic_rating
