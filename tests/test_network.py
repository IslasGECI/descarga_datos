import descarga_datos
import os
from descarga_datos import download_file_from_repo

if not os.path.exists("./results"):
    os.mkdir("./results")


def test_download_file_from_repo():
    archivo = descarga_datos.internals.DataFile(
        "tabular_data_packages",
        "esfuerzos_capturas_gatos_socorro",
        "captura_gatos_socorro.csv",
        "a3e8",
        "csv",
    )
    url = archivo.get_url_to_file()
    destination_folder = "./results"
    download_file_from_repo(url, destination_folder)
