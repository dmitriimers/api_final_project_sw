import json
from requests import Response
"""Methods to check our requests"""


class Checking():

    """Method to check a status code"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Success!!! Status code = " + str(response.status_code))
        else:
            print("Fail!!! Status code = " + str(response.status_code))


    # """Method to check necessary fields in response"""
    #
    # @staticmethod
    # def check_json_token(response: Response, expected_value):
    #     token = json.loads(response.text)
    #     assert list(token) == expected_value
    #     print("All input fields are correct")
    #
    #
    # """Method to check values of necessary fields in response"""
    #
    # @staticmethod
    # def check_json_value(response: Response, field_name, expected_value):
    #     check = response.json()
    #     check_info = check.get(field_name)
    #     assert check_info == expected_value
    #     print(f'{field_name} is correct!!!')
    #
    # """Method to check values of necessary fields in response by a specific word"""
    #
    # @staticmethod
    # def check_json_search_word_in_value(response: Response, field_name, search_word):
    #     check = response.json()
    #     check_info = check.get(field_name)
    #     if search_word in check_info:
    #         print(f'Word {search_word} is in field!!!')
    #     else:
    #         print(print(f'Word {search_word} is not in field!!!'))