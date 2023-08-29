import json
from requests import Response
from utils.http_methods import HttpMethods
from utils.api import SWAPI_api

"""Get list of films with Darth Vader, then get all characters names"""
class TestGetCharacterInfo():

    def test_get_all_characters(self):
        print("Get method list of films")
        result_get = SWAPI_api.get_list_of_films(self)

        print("Get characters who was in films with Darth Vader")
        SWAPI_api.get_characters_from_films_with_darth_vader(result_get)

