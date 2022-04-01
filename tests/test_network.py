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
    getter_size_file = Getter_File_Size(file)
    file_size = getter_size_file.get_size()
    return file_size


class Getter_File_Size:
    def __init__(self, file):
        self.destination_folder = "./results"
        self.file = file
        self.path = None

    def get_size(self):
        self._ensure_file_do_not_exist()
        self._download_the_file()
        file_size = os.path.getsize(self.path)
        remove_file(self.path)
        return file_size

    def _ensure_file_do_not_exist(self):
        self.path = f"{self.destination_folder}/{self.file.filename}"
        remove_file(self.path)
    
    def _download_the_file(self):
        url = self.file.get_url_to_file()
        download_file_from_repo(url, self.destination_folder)
