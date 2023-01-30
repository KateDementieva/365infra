import random


class AllUsersResponse:
    def __init__(self, code, users_list):
        self._code = code
        self._users_list = users_list

    def get_status_code(self):
        return self._code

    def get_random_user(self):
        return random.choice(self._users_list)
