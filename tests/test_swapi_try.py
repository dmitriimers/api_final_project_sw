import requests

class TestSwapiTry:

    def test_swapi_try(self):
        base_url = "https://swapi.dev/api/"             # base url
        get_resource = "people/4/"
        get_url = (f"{base_url}{get_resource}")
        print(get_url)
        result = requests.get(get_url)
        print(result.text)
        # return result
        result_films = result.json().get("films")
        print(result_films)