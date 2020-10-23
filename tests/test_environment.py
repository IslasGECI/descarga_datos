import os

from descarga_datos import get_user_from_enviorment_variable
from descarga_datos import get_password_from_enviormet_variable

os.environ["BITBUCKET_USERNAME"] = "user"
os.environ["BITBUCKET_PASSWORD"] = "password"


def test_get_user_from_enviorment_variable():
    obtained_user = get_user_from_enviorment_variable()
    expected_user = os.environ["BITBUCKET_USERNAME"]
    assert expected_user == obtained_user


def test_get_password_from_enviormet_variable():
    obtained_password = get_password_from_enviormet_variable()
    expected_password = os.environ["BITBUCKET_PASSWORD"]
    assert expected_password == obtained_password
