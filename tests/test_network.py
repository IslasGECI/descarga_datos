import descarga_datos
import os
from descarga_datos import download_file_from_repo
import pytest

if not os.path.exists("./results"):
    os.mkdir("./results")

test_data = [
    ("tabular_data_packages", "captura_gatos_socorro.csv", True),
    ("archivos_binarios", "clarion_vegetal_types.zip", True),
    ("archivos_binarios", "XXclarion_vegetal_types.zipXX", False),
]


@pytest.mark.parametrize("repo, filename, is_a_file", test_data, ids=["CSV", "ZIP", "Not a file"])
def test_download_file_from_repo(repo, filename, is_a_file):
    file = set_file(repo, filename)
    assert_can_download_a_file(file, is_a_file)


def set_file(repo, filename):
    file_setter = {
        "archivos_binarios": set_binary_file,
        "tabular_data_packages": set_tdp_file,
    }
    return file_setter[repo](filename)


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


def assert_can_download_a_file(file, is_a_file):
    FILE_SIZE_CUTOFF = 200
    file_size = get_file_size(file)
    is_big_enough = file_size > FILE_SIZE_CUTOFF
    assert is_big_enough == is_a_file


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
