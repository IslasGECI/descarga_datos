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
    assert_can_download_a_file(file_name, destination_folder)
    file_name = "XXclarion_vegetal_types.zipXX"
    assert_can_not_download_a_file(file_name, destination_folder)


def get_file_size(file_name,destination_folder):
    archivo = descarga_datos.internals.DataFile(
        "archivos_binarios",
        "shp/clarion_vegetal_zones",
        file_name,
        "aeafdde",
        "zip",
    )
    url = archivo.get_url_to_file()
    download_file_from_repo(url, destination_folder)
    return os.path.getsize(f"{destination_folder}/{file_name}")


def assert_can_download_a_file(file_name,destination_folder):
    file_size = get_file_size(file_name,destination_folder)
    assert file_size > 200


def assert_can_not_download_a_file(file_name,destination_folder):
    file_size = get_file_size(file_name,destination_folder)
    assert file_size <= 200
