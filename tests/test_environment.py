import os

from descarga_datos import get_email_from_environment_variable
from descarga_datos import get_token_from_environment_variable


def test_get_token_from_environment_variable():
    obtained_token = get_token_from_environment_variable()
    expected_token = os.environ["BITBUCKET_API_TOKEN"]
    assert expected_token == obtained_token


def test_get_email_from_environment_variable():
    obtained_email = get_email_from_environment_variable()
    expected_email = os.environ["BITBUCKET_EMAIL"]
    assert expected_email == obtained_email
