from .internals import Analysis
from .network import download_file_from_repo
from .utils import get_password_from_enviormet_variable, get_user_from_enviorment_variable
import sys
import json


def descarga_archivo(file_name, destination_folder):
    with open("analyses.json") as json_analyses:
        lista_analisis = json.load(json_analyses)
    for diccionario_analisis in lista_analisis:
        analisis = Analysis(**diccionario_analisis)
        if analisis.is_dependent_on_datafile(file_name):
            download_file_from_repo(
                analisis.get_url_to_datafile(file_name),
                destination_folder,
                get_user_from_enviorment_variable(),
                get_password_from_enviormet_variable(),
            )


def cli():
    descarga_archivo(*sys.argv[1:])
