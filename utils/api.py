from utils.http_methods import HttpMethods
import requests

"""Methods for testing SWAPI"""

base_url = "https://swapi.dev/api/"             # base url

class SWAPI_api():

    """Method to get a list of films for a character Darth Vader"""

    @staticmethod
    def get_list_of_films(self):
        get_resource = "people/4/"  # Resource of get method
        get_url = (f"{base_url}{get_resource}")   #Full url to get method
        print(get_url)
        result = HttpMethods.get(get_url)
        print(result.text)git
        result_films = result.json().get("films")
        print(f'List of film urls with Darth Vader: {result_films}')
        return result_films


    """Method to get a list of characters urls then get names and save them into a txt file"""
    @staticmethod
    def get_characters_from_films_with_darth_vader(result_films):
        result_characters_no_duplicates = set()    # Create an empty set
        for films_url in result_films:
            print(films_url)
            result = HttpMethods.get(films_url)
            result_characters = result.json().get("characters")
            result_characters_no_duplicates.update(result_characters)    # Update previously created set
            print(result_characters_no_duplicates)

        """Get names of different characters using set of urls"""
        count = 0
        for names_url in result_characters_no_duplicates:
            print(names_url)
            result_names = HttpMethods.get(names_url)
            result_names_list = result_names.json().get("name")
            count += 1


            """Block with a file creation"""
            sw_names = open('docs/sw_names.txt', 'a', encoding='utf-8')
            sw_names.write(result_names_list + "\n")
            sw_names.close()

        print(f'Number of iterations: {count}')