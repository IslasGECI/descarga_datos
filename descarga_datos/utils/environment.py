import os


def get_user_from_environment_variable() -> str:
    """
    Return the Bitbucket username from the BITBUCKET_USERNAME environment
    variable.

    Examples
    --------
    Get username
    >>> user = descarga_datos.get_user_from_environment_variable()
    """
    return os.environ["BITBUCKET_USERNAME"]


def get_password_from_environment_variable() -> str:
    """
    Return the Bitbucket password from the BITBUCKET_PASSWORD environment
    variable.

    Examples
    --------
    Get password
    >>> password = descarga_datos.get_password_from_environment_variable()
    """
    return os.environ["BITBUCKET_PASSWORD"]


def get_token_from_environment_variable() -> str:
    """
    Return the Bitbucket API token from the BITBUCKET_API_TOKEN environment
    variable.

    Examples
    --------
    Get token
    >>> token = descarga_datos.get_token_from_environment_variable()
    """
    return os.environ["BITBUCKET_API_TOKEN"]


def get_email_from_environment_variable() -> str:
    """
    Return the Bitbucket email from the BITBUCKET_EMAIL environment variable.

    Examples
    --------
    Get email
    >>> email = descarga_datos.get_email_from_environment_variable()
    """
    return os.environ["BITBUCKET_EMAIL"]
