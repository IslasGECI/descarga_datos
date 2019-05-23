import os


def get_user_from_enviorment_variable() -> str:
    return os.environ["BITBUCKET_USERNAME"]


def get_password_from_enviormet_variable() -> str:
    return os.environ["BITBUCKET_PASSWORD"]
