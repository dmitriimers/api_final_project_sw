import requests

"""List of http methods"""


class HttpMethods:

    @staticmethod
    def get(url):
        result = requests.get(url)
        return result

