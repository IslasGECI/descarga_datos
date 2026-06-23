from descarga_datos.utils import (
    get_email_from_environment_variable,
    get_token_from_environment_variable,
)


class DataFile:
    """
    Represents a data file specified as a dependency of an analysis in
    analyses.json.

    Parameters
    ----------
    `source : str`
        Name of the repository where the data is stored

    `path : str`
        Path to the data inside the repository

    `filename : str`
        Name of the data file

    `version : str`
        Commit hash of the version where the data was committed

    `type : str`
        String representing the data type, e.g. datapackage, gpx, csv, excel

    Attributes
    ----------
    `filename : str`
        Name of the file

    `path : str`
        Path of the file within the repository

    Methods
    -------
    `get_url_to_file(): str`
        Returns the URL from which the data file can be downloaded

    Notes
    -----
    None

    Examples
    --------
    Create a file
    >>> file = descarga_datos.internals.DataFile("repo_datos_inventado", "carpeta_datos",
                                                  "datos.csv", "9cc34")
    Get file URL
    >>> file.get_url_to_file()
    'https://bitbucket.org/IslasGECI/repo_datos_inventado/raw/9cc34/carpeta_datos/datos.csv'
    """

    def __init__(self, source: str, path: str, filename: str, version: str, type: str):
        self._source = source
        self._path = path
        self._filename = filename
        self._version = version
        self._type = type

    @property
    def filename(self):
        """
        Return the name of the file.
        """
        return self._filename

    @property
    def path(self):
        """
        Return the path of the file.
        """
        return self._path

    def get_url_to_file(self) -> str:
        """
        Returns the URL to download the file from Bitbucket.

        Examples
        --------
        Get file URL
        >>> archivo = descarga_datos.internals.DataFile("repo_datos_inventado", "carpeta_datos",
                                                         "datos.csv", "9cc34")
        >>> archivo.get_url_to_file()
        'https://user:password@api.bitbucket.org/2.0/repositories/IslasGECI/repo_datos/src/9cc34/carpeta_datos/datos.csv'
        """
        bitbucket_email = get_email_from_environment_variable()
        bitbucket_token = get_token_from_environment_variable()
        base_url = f"https://{bitbucket_email}:{bitbucket_token}@api.bitbucket.org/2.0/repositories/IslasGECI/"
        return base_url + f"{self._source}/src/{self._version}/{self._path}/{self._filename}"
