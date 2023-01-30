from api_tests.models.payloads.post_payload import PostPayload
from api_tests.requests.posts import create_post, get_all_posts
from api_tests.requests.users import get_users
from util.string_utils import get_random_string

BASE_URL = "https://jsonplaceholder.typicode.com/"


def test_can_call_endpoint():
    """
    Check that GET /users endpoint is callable and returns response with status code 200
    """
    response = get_users()
    assert response.get_status_code() == 200, "Response status code of GET /users call must be 200"


def test_can_do_a_post():
    """
    Check possibility to receive all users list, verify that post ID is in range from 1 to 100 and create a new post
    """
    all_users_response = get_users()
    assert all_users_response.get_status_code() == 200, "Response status code of GET /users call must be 200"

    random_user = all_users_response.get_random_user()
    all_posts = get_all_posts()
    user_posts = all_posts.get_posts_for_user(random_user["id"])
    for post in user_posts:
        assert 1 <= post["id"] <= 100, "Post ID must be integer between 1 and 100"

    payload = PostPayload(get_random_string(10), get_random_string(20), random_user["id"]).to_json()
    create_post_response = create_post(payload)

    assert create_post_response.get_status_code() == 201, "Response status code of POST /posts call must be 201"
    assert 1 <= create_post_response.get_post_id() <= 100, "New post ID must be integer between 1 and 100"
