import os


def get_user_from_environment_variable() -> str:
    """
    Función que regresa el nombre de usuario de Bitbucket desde la variable de
    entorno BITBUCKET_USERNAME

    Parámetros
    ----------
    Ninguno

    Notas
    -----
    Ninguna

    Ejemplos
    --------
    Obtener nombre de usuario
    >>> usuario = descarga_datos.util.get_user_from_environment_variable()
    """
    return os.environ["BITBUCKET_USERNAME"]


def get_password_from_environment_variable() -> str:
    """
    Función que regresa la contraseña de Bitbucket desde la variable de entorno
    BITBUCKET_PASSWORD

    Parámetros
    ----------
    Ninguno

    Notas
    -----
    Ninguna

    Ejemplos
    --------
    Obtener contraseña del usuario
    >>> contrasenia = descarga_datos.util.get_password_from_environment_variable()
    """
    return os.environ["BITBUCKET_PASSWORD"]


def get_token_from_environment_variable() -> str:
    """
    Función que regresa el token de Bitbucket desde la variable de entorno
    BITBUCKET_API_TOKEN

    Parámetros
    ----------
    Ninguno

    Notas
    -----
    Ninguna

    Ejemplos
    --------
    Obtener token
    >>> token = descarga_datos.util.get_token_from_environment_variable()
    """
    return os.environ["BITBUCKET_API_TOKEN"]


def get_email_from_environment_variable() -> str:
    """
    Función que regresa el correo electrónico de Bitbucket desde la variable de
    entorno BITBUCKET_EMAIL

    Parámetros
    ----------
    Ninguno

    Notas
    -----
    Ninguna

    Ejemplos
    --------
    Obtener correo electrónico
    >>> email = descarga_datos.util.get_email_from_environment_variable()
    """
    return os.environ["BITBUCKET_EMAIL"]
