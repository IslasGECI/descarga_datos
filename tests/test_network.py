import descarga_datos
import os
from descarga_datos import download_file_from_repo

if not os.path.exists("./results"):
    os.mkdir("./results")


def test_download_file_from_repo():

    filename = "captura_gatos_socorro.csv"
    file = set_tdp_file(filename)
    assert_can_download_a_file(file)

    filename = "clarion_vegetal_types.zip"
    file = set_binary_file(filename)
    assert_can_download_a_file(file)

    filename = "XXclarion_vegetal_types.zipXX"
    file = set_binary_file(filename)
    assert_can_not_download_a_file(file)


def set_binary_file(filename):
    return descarga_datos.internals.DataFile(
        "archivos_binarios",
        "shp/clarion_vegetal_zones",
        filename,
        "aeafdde",
        "zip",
    )


def set_tdp_file(filename):
    return descarga_datos.internals.DataFile(
        "tabular_data_packages",
        "esfuerzos_capturas_gatos_socorro",
        filename,
        "a3e8",
        "csv",
    )


def get_file_size(file):
    url = file.get_url_to_file()
    destination_folder = "./results"
    download_file_from_repo(url, destination_folder)
    return os.path.getsize(f"{destination_folder}/{file.filename}")


FILE_SIZE_CUTOFF = 200


def assert_can_download_a_file(file):
    file_size = get_file_size(file)
    assert file_size > FILE_SIZE_CUTOFF


def assert_can_not_download_a_file(file):
    file_size = get_file_size(file)
    assert file_size <= FILE_SIZE_CUTOFF
