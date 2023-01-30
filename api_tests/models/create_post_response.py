
class CreatePostResponse:
    def __init__(self, code, id):
        self._code = code
        self._id = id

    def get_status_code(self):
        return self._code

    def get_post_id(self):
        return self._id
