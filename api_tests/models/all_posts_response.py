
class AllPostsResponse:
    def __init__(self, code, posts_list):
        self._code = code
        self._posts_list = posts_list

    def get_posts_for_user(self, user_id):
        return filter(lambda post: post["userId"] == user_id, self._posts_list)
