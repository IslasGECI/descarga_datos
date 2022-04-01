import descarga_datos
import os
from descarga_datos import download_file_from_repo

if not os.path.exists("./results"):
    os.mkdir("./results")


def test_download_file_from_repo():

    filename = "captura_gatos_socorro.csv"
    file = set_file("tabular_data_packages",filename)
    assert_can_download_a_file(file)

    filename = "clarion_vegetal_types.zip"
    file = set_file("archivos_binarios",filename)
    assert_can_download_a_file(file)

    filename = "XXclarion_vegetal_types.zipXX"
    file = set_file("archivos_binarios",filename)
    assert_can_not_download_a_file(file)


def set_file(repo,filename):
    selector = {
            "archivos_binarios": set_binary_file,
            "tabular_data_packages": set_tdp_file,
            }
    return selector[repo](filename)

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


def remove_file(path):
    if os.path.exists(path):
        os.remove(path)


def get_file_size(file):
    destination_folder = "./results"
    path = f"{destination_folder}/{file.filename}"
    remove_file(path)
    url = file.get_url_to_file()
    download_file_from_repo(url, destination_folder)
    file_size = os.path.getsize(path)
    remove_file(path)
    return file_size


FILE_SIZE_CUTOFF = 200


def assert_can_download_a_file(file):
    file_size = get_file_size(file)
    assert file_size > FILE_SIZE_CUTOFF


def assert_can_not_download_a_file(file):
    file_size = get_file_size(file)
    assert file_size <= FILE_SIZE_CUTOFF
