import pytest

from api_tests.db.db_service import UsersDbService


@pytest.mark.usefixtures("setup_db")
def test_get(session):
    users = UsersDbService(session)
    users.add_user('Alex', True)
    users.add_user('Nina', False)
    users.add_user('David', False)

    assert users.get_activity('Alex')[0] is 1, "Alex must be active user"
