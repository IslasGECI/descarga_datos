import os


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
