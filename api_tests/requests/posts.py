import environment
import allure
import requests

from api_tests.models.all_posts_response import AllPostsResponse
from api_tests.models.create_post_response import CreatePostResponse


@allure.step("Get all posts")
def get_all_posts():
    response = requests.get(environment.BASE_URL + "posts")
    return AllPostsResponse(response.status_code, response.json())


@allure.step("Create new post")
def create_post(payload):
    response = requests.post(environment.BASE_URL + "posts", payload)
    json = response.json()
    return CreatePostResponse(response.status_code, response.json()["id"])
