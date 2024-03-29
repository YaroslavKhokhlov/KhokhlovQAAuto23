import pytest
from modules.api.clients.github import Github

class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Yaroslav"
        self.second_name = "Khokhlov"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


def test_change_name(user):
    assert user.name == 'Sergii'


def test_change_second_name(user):
    assert user.second_name == 'Butenko'

@pytest.fixture
def github_api():
    api = Github()
    yield api