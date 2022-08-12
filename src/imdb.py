import requests


class Imdb:
    """A wrapper class for the IMDb-API."""

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = 'https://imdb-api.com/en/API'

    def search(self, name: str, search_type: str = 'movie') -> list[dict]:
        """Searches for occurences of movies or series whose title/description matches the specified name.

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
            id, title, description, image_url."""

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

    def details(self, id: str) -> dict:
        """Searches for details of the title specified by its id.

        Parameters
        ----------
        id : str
            The id of the title to search.

        Returns
        -------
        dict
            A dictionary with the following properties:
            title, genres, languages, type (movie or series), year, image_url, runtime,
            plot, directors, stars, content_rating, imdb_rating, imdb_votes, metacritic_rating."""

        url = f'{self.base_url}/Title/{self.api_key}/{id}'
        response = requests.get(url)
        details: dict = {}

        if response.status_code == 200:
            response_obj: dict = response.json()
            details = {
                'title': self.__safe_get(response_obj, 'fullTitle'),
                'genres': self.__safe_get(response_obj, 'genres'),
                'languages': self.__safe_get(response_obj, 'languages'),
                'type': self.__safe_get(response_obj, 'type'),
                'year': self.__safe_get(response_obj, 'year'),
                'image_url': self.__safe_get(response_obj, 'image'),
                'runtime': self.__safe_get(response_obj, 'runtimeStr'),
                'plot': self.__safe_get(response_obj, 'plot'),
                'directors': self.__safe_get(response_obj, 'directors'),
                'stars': self.__safe_get(response_obj, 'stars'),
                'content_rating': self.__safe_get(response_obj, 'contentRating'),
                'imdb_rating': self.__safe_get(response_obj, 'imDbRating'),
                'imdb_votes': self.__safe_get(response_obj, 'imDbRatingVotes'),
                'metacritic_rating':  self.__safe_get(response_obj, 'metacriticRating')
            }

        return details

    def __safe_get(self, arg: dict, key: str) -> str:
        return arg.get(key) or '?'
