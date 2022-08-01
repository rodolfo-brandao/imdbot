import requests


class Imdb:
    '''
    A wrapper class for the IMDb API.
    '''

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = 'https://imdb-api.com/en/API'

    def search(self, name: str, search_type: str = 'movie') -> list[dict]:
        '''
        Searches for occurences of movies or series whose title matches the specified name.

        Parameters
        ----------
        name : str
            The name to search.
        search_type: str (default: "movie")
            The type of the search. It can be "movie" or "series".

        Returns
        -------
        list[dict]
            A list containing dictionaries with the following properties:
            id, title, description, image_url.
        '''

        occurences: list[dict] = []
        endpoint = 'SearchSeries' if search_type == 'series' else 'SearchMovie'
        url = f'{self.base_url}/{endpoint}/{self.api_key}/{name}'

        response = requests.get(url)

        if response.status_code == 200:
            response_obj = response.json()

            for occurence in response_obj['results']:
                occurences.append({
                    'id': occurence['id'],
                    'title': occurence['title'],
                    'description': occurence['description'],
                    'image_url': occurence['image']
                })

        return occurences

    def search_title(self, title_id: str) -> dict:
        '''
        Searchs for the title specified by the id.

        Parameters
        ----------
        id : str
            The id of the title to search.

        Returns
        -------
        dict
            A dictionary with the following properties:
            title, genres, languages, type (movie or series), year, image_url, runtime,
            plot, directors, stars, content_rating, imdb_rating, imdb_votes, metacritic_rating.
        '''

        url = f'{self.base_url}/Title/{self.api_key}/{title_id}'

        response = requests.get(url)

        if response.status_code == 200:
            response_obj = response.json()
            return {
                'title': response_obj['fullTitle'],
                'genres': response_obj['genres'],
                'languages': response_obj['languages'],
                'type': response_obj['type'],
                'year': response_obj['year'],
                'image_url': response_obj['image'],
                'runtime': response_obj['runtimeStr'],
                'plot': response_obj['plot'],
                'directors': response_obj['directors'],
                'stars': response_obj['stars'],
                'content_rating': response_obj['contentRating'],
                'imdb_rating': response_obj['imDbRating'],
                'imdb_votes': response_obj['imDbRatingVotes'],
                'metacritic_rating': response_obj['metacriticRating']
            }

        return {}
