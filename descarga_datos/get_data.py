import urllib.request


def download_file_from_repo(url: str, destionation_filename: str, user: str, password: str):
    """
    Función que permite descargar archivos desde repositorios de bitbucket

    Parámetros
    ----------
    `url : str`
        Dirección de Bitbucket donde se encuentra el archivo

    `destionation_filename: str`
        Nombre y dirección del archivo donde se guardarán los datos descargados

    `user : str`
        Nombre de usuario de Bitbucket

    `password : str`
        Contraseña del usuario
    
    Notas
    -----
    Ninguna
    
    Ejemplos
    --------
    Descargar un archivo
    >>> url = 'https://bitbucket.org/usuario_prueba/repo_datos/raw/9fd54/datos.xlsx'
    >>> download_file(url, 'inst/extdata/datos.xlsx', os.environ['BITBUCKET_USERNAME'],
    ... os.environ['BITBUCKET_PASSWORD'])
    """
    manejador_autenticacion = urllib.request.HTTPBasicAuthHandler()
    manejador_autenticacion.add_password(None, uri=url, user=user, passwd=password)
    conexion = urllib.request.build_opener(manejador_autenticacion)
    urllib.request.install_opener(conexion)
    urllib.request.urlretrieve(url, filename)
