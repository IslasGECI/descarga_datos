import os

from descarga_datos import get_user_from_enviorment_variable
from descarga_datos import get_password_from_enviormet_variable

os.environ["BITBUCKET_USERNAME"] = "user"
os.environ["BITBUCKET_PASSWORD"] = "password"


def test_get_user_from_enviorment_variable():
    assert os.environ["BITBUCKET_USERNAME"] == get_user_from_enviorment_variable()


def test_get_password_from_enviormet_variable():
    assert os.environ["BITBUCKET_PASSWORD"] == get_password_from_enviormet_variable()
