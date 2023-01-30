import json


class PostPayload:
    title: str
    body: str
    userId: int

    def __init__(self, title, body, userId):
        self.title = title
        self.body = body
        self.userId = userId

    def to_json(self):
        return json.dumps(self.__dict__)

    def get_user_is_as_str(self):
        return str(self.userId)
