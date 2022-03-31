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
    file_name = "clarion_vegetal_types.zip"
    archivo = descarga_datos.internals.DataFile(
        "archivos_binarios",
        "shp/clarion_vegetal_zones",
        file_name,
        "aeafdde",
        "zip",
    )
    url = archivo.get_url_to_file()
    download_file_from_repo(url, destination_folder)
    file_size = os.path.getsize(f"{destination_folder}/{file_name}")
    assert file_size > 200
