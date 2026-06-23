import os
import requests


def download_file_from_repo(url: str, filename: str):
    """
    Downloads a file from a Bitbucket repository.

    Parameters
    ----------
    `url : str`
        URL of the file in the Bitbucket repository

    `filename : str`
        Local path where the downloaded file will be saved

    Examples
    --------
    Download a file
    >>> url = 'https://bitbucket.org/usuario_prueba/repo_datos/raw/9fd54/datos.xlsx'
    >>> download_file_from_repo(url, 'inst/extdata/datos.xlsx')
    """
    directory = os.path.split(url)[1]
    path = os.path.join(filename, directory)
    response = requests.request("GET", url)
    with open(path, "wb") as f:
        f.write(response.content)
