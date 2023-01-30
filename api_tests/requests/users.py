import environment
import allure
import requests

from api_tests.models.all_users_response import AllUsersResponse


@allure.step("Get all users")
def get_users():
    response = requests.get(environment.BASE_URL + "users")
    return AllUsersResponse(response.status_code, response.json())
